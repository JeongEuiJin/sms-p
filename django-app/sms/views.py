import sys

from django.http import HttpResponse
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from django.shortcuts import render

from sms.forms import SmsForm

api_key = "NCSGLMHSQ2FTVZUA"
api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"

def sms_send(request):
    form = SmsForm()
    params = dict()
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            params['type'] = form.cleaned_data['type']
            params['to'] = form.cleaned_data['to']
            params['from'] = '01029953874'
            params['text'] =form.cleaned_data['text']
        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : {}" .format(response['success_count']))
            print("Error Count : %s" .format(response['error_count']))
            print("Group ID : %s".format(response['group_id']))

            if "error_list" in response:
                print("Error List : %s".format(response['error_list']))

        except CoolsmsException as e:
            print("Error Code : %s".format(e.code))
            print("Error Message : %s".format(e.msg))

            sys.exit()

        return HttpResponse('successful')

    context = {
        'form': form,
    }

    return render(request, 'sms/sms_send.html', context)
    # if __name__ == "__main__":
    #
    #     ## 4 params(to, from, type, text) are mandatory. must be filled
    #
    #     cool = Message(api_key, api_secret)
    #
    #
    #
    #     try:
    #         response = cool.send(params)
    #         print("Success Count : %s" % response['success_count'])
    #         print("Error Count : %s" % response['error_count'])
    #         print("Group ID : %s" % response['group_id'])
    #
    #         if "error_list" in response:
    #             print("Error List : %s" % response['error_list'])
    #
    #     except CoolsmsException as e:
    #         print("Error Code : %s" % e.code)
    #         print("Error Message : %s" % e.msg)
    #     sys.exit()
