from django.http import JsonResponse
from django.views import View
from app.models import Chat, Keyword
from json import loads


class WebhookView(View):

    def post(self, request):

        try:
            empty_message = { 'response': 'none' }
            response  = JsonResponse(empty_message)

            body = loads(request.body)
            if 'message' in body:   
                body_chat = body['message']['chat']
                body_from = body['message']['from']
                text = ""

                if "text" in body['message']:
                    body_text = str(body['message']['text']).lower().split()

                    if len(body_text) == 1:
                        for keyword in body_text:
                            
                            if keyword == '/start':
                                text = ""
                                if body_chat['type'] == 'private':
                                    name = ""
                                    if "first_name" in body_from: name += body_from['first_name'] + " "
                                    if "last_name" in body_from: name += body_from['last_name'] + " "
                                    if "username" in body_from: name += "@" + body_from['username']
                                    if Chat.objects.filter(chat_id=body_from['id']):
                                        chat = Chat.objects.get(chat_id=body_from['id'])
                                        chat.name = name
                                        chat.details = body
                                        chat.tipology = body_chat['type']
                                        chat.save()
                                    else:
                                        chat = Chat.objects.create(chat_id=body_from['id'], name=name, details=body)
                                        chat.save()
                                    text = "Bot Enabled!"
                                else:
                                    text = "Bot Enabled in Group!"

                            elif keyword == '/info':
                                text = "Info Telegram Answer Bot!"
                                
                            else:
                                if keyword.startswith('/'):
                                    keyword = keyword[1:]
                                try:
                                    result = Keyword.objects.get(keyword=keyword, enable=True)                                    
                                    text = str(result.answer)
                                except Keyword.DoesNotExist:
                                    result = None

                    else:
                        keywords = str(body['message']['text']).lower()
                        try:
                            result = Keyword.objects.get(keyword=keywords, enable=True)
                            text = str(result.answer)
                        except Keyword.DoesNotExist:
                            result = None
                            multiple_answer = ""
                            for keyword in body_text:
                                try:
                                    for result in Keyword.objects.filter(keyword__contains=keyword, enable=True):
                                        multiple_answer += "- " + result.answer + "\n"
                                except Keyword.DoesNotExist:
                                    result = None
                            if result:
                                text = "Possible answers:\n" + multiple_answer

                if text:
                    message = {
                        'chat_id':      body_chat['id'], 
                        'text':         text, 
                        "method":       'sendMessage' 
                    }
                    response  = JsonResponse(message)
        
        
        except Exception as e:
            print("webhook error: {0}".format(e))
            error_message = { 'response': 'webhook error' }
            response  = JsonResponse(error_message)
            pass
            
        return response

