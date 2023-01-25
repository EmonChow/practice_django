import requests

from member.models import ExecutiveMember


def sendSms(mobile: str, message: str) -> dict:
    mobile = str(mobile)[-11:]
    phone_numbers = [profile.primary_phone for profile in ExecutiveMember.objects.all()]
    for phn in phone_numbers:
        print(phn)
    # url = f"https://sms.bluebayit.com/httpapi/sendsms?userId=bluebay&password=bluebayit7811&smsText={message}" \
    #       f"&commaSeperatedReceiverNumbers={mobile}&nameToShowAsSender={phn}"
    # res = requests.get(url)
    #
    # print('res: ', res)
    # print('res.json(): ', res.json())
    #
    # return res.json()
