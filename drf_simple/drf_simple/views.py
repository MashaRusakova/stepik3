import requests
from pip._internal.utils import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(http_method_names=['GET'])
def beautybox_list(request: Request) -> Response:
    response = requests.get('https://stepik.org/media/attachments/course/73594/beautyboxes.json')
    result = []

    beautyboxes = response.json()

    if request.query_params:
        price = request.query_params.get('min_price', 0)
        weight = request.query_params.get('min_weight', 0)

        if not (price or weight):
            return Response(status=status.HTTP_404_NOT_FOUND)

        for box in beautyboxes:
            if (box['price'] >= int(price)) or (box['weight_grams'] >= int(weight)):

                result.append(box)
    else:
        result = beautyboxes

    result_formatted = []
    for box in result:
        listdata = {}
        listdata['name'] = box.get('name')
        listdata['about'] = box.get('about')
        listdata['weight_grams'] = box.get('weight_grams')
        listdata['price'] = box.get('price')
        result_formatted.append(listdata)

    return Response(result_formatted)


@api_view(http_method_names=['GET'])
def beautybox_content(request: Request, pk: int) -> Response:
    response = requests.get('https://stepik.org/media/attachments/course/73594/beautyboxes.json')
    beautyboxes = response.json()

    for beautybox_item in beautyboxes:
        if beautybox_item['inner_id'] == pk:
            response = beautybox_item
            listdata = {}
            listdata['name'] = beautybox_item.get('name')
            listdata['about'] = beautybox_item.get('about')
            listdata['weight_grams'] = beautybox_item.get('weight_grams')
            listdata['price'] = beautybox_item.get('price')
            beautyboxes = listdata

    if response:
        return Response(beautyboxes)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def recipient_list(request: Request) -> Response:
    response = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    list = []
    listdata = {}

    if response.status_code != 200:
        return Response(status=status.HTTP_409_CONFLICT)
    try:
        recipients = response.json()
        for item in recipients:
            listdata.update(item['info'])
            listdata.update(item['contacts'])
            list.append(listdata)
            listdata = {}
        recipients = list

    except Exception as ex:
        pass
    else:
        return Response(recipients)


@api_view(http_method_names=['GET'])
def recipient_content(request: Request, pk: int) -> Response:
    response = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    listdata = {}
    recipients = response.json()

    for recipient_item in recipients:
        if recipient_item['id'] == pk:
            response = recipient_item
            listdata.update(recipient_item['info'])
            listdata.update(recipient_item['contacts'])
        recipients = listdata

    if response:
        return Response(recipients)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


