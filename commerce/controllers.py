from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4

from commerce.models import *
from commerce.schemas import *
from config.utils.schemas import MessageOut

User = get_user_model()

#commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])

commerce_controller = {'products': Router(tags=['products']),'notifications': Router(tags=['notifications']), 'Service': Router(tags=['Service']),
                     'Center': Router(tags=['Center']),'Advertising' : Router(tags=['Advertising']),
                     'Center_images' : Router(tags=['Center_image']),'News' : Router(tags=['News']), 'Service_images' : Router(tags=['Service_image']),
                       'Center_opinions' : Router(tags=['Center_opinion']),'Service_opinions' : Router(tags=['Service_opinion']),'Reservation' : Router(tags=['Reservation']),
                       }



@commerce_controller['notifications'].get('notifications', response={
    200: List[notifications], })
def list_notifications(request, title: str = None,sender: str = None, discription: str = None):
     notifications = notification.objects.all()
     return notifications

@commerce_controller['notifications'].get('notifications/{id}', response={
    200: notifications
})
def retrieve_notifications(request, id):
    return get_object_or_404(notification, id=id)


@commerce_controller['notifications'].get('notifications', response={
    200: List[notifications], })
def list_notifications(request):
    notifications = notification.objects.all()
    return notifications


@commerce_controller['notifications'].post('notifications', response={
    201: notificationsOut,
    400: MessageOut
})
def create_notifications(request, payload: update_notifications):
    try:
        notf = notification.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, notf


@commerce_controller['notifications'].get('notifications/{id}', response={
    200: notificationsOut
})
def retrieve_notifications(request, id):
    return get_object_or_404(notification, id=id)


@commerce_controller['notifications'].put('notifications/{id}', response={200: update_notifications})
def update_notification(request, id: UUID4, payload: update_notifications):
    updateNotf = get_object_or_404(notification, id=id)
    for attr, value in payload.dict().items():
        setattr(updateNotf, attr, value)
    updateNotf.save()
    return updateNotf


@commerce_controller['notifications'].delete('notifications/{id}')
def delete_notification(request, id: UUID4):
    deleted = get_object_or_404(notification, id=id)
    deleted.delete()
    return 200, {'detail': 'deleted'}


###################################################

@commerce_controller['Service'].get('Services', response={
    200:List[ServiceOut], })
def list_services(request):
    srv = service.objects.all()
    return srv


@commerce_controller['Service'].post('service', response={
    201: ServiceOut,
    400: MessageOut
})
def create_Service(request, payload: Services):
    try:
        srv = service.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, srv


@commerce_controller['Service'].get('service/{id}', response={
    200: ServiceOut
})
def retrieve_service(request, id):
    return get_object_or_404(service, id=id)


@commerce_controller['Service'].put('service/{id}', response={200: update_Services})
def update_service(request, id: UUID4, payload: update_Services):
    updatesrv = get_object_or_404(service, id=id)
    for attr, value in payload.dict().items():
        setattr(updatesrv, attr, value)
    updatesrv.save()
    return updatesrv


@commerce_controller['Service'].delete('service/{id}')
def delete_service(request, id: UUID4):
    srv = get_object_or_404(service, id=id)
    srv.delete()
    return 200, {'detail': 'deleted'}


@commerce_controller['Service'].get('Search', response={
    200: List[ServiceOut],
})
def search_service(request, q: str = None,):
    service = Services.objects.all()

    if q:
        service = service.filter(
            Q(nameicontains=q) | Q(descriptionicontains=q)
        )

    """if price_lte:
        service = service.filter(discounted_pricelte=price_lte)

    if price_gte:
        service = service.filter(discounted_pricegte=price_gte)"""

    return service

#######################################


@commerce_controller['Service_images'].get('Service_image', response={
    200:List[ImageOut_S], })
def list_images(request):
    img = Service_image.objects.all()
    return img


@commerce_controller['Service_images'].post('Service_image', response={
    201: ImageOut_S,
    400: MessageOut
})
def create_image(request, payload: ImageOut_S):
    try:
        img = Service_image.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, img

@commerce_controller['Service_images'].put('Service_image/{id}', response={200: update_Images_S})
def update_image(request, id: UUID4, payload: update_Images_S):
    updateimg = get_object_or_404(Service_image, id=id)
    for attr, value in payload.dict().items():
        setattr(updateimg, attr, value)
    updateimg.save()


@commerce_controller['Service_images'].delete('Service_image/{id}')
def delete_Images(request, id: UUID4):
    img = get_object_or_404(Service_image, id=id)
    img.delete()

################################################33


@commerce_controller['Center_images'].get('Center_image', response={
    200:List[ImageOut_C], })
def list_images(request):
    img = Center_image.objects.all()
    return img


@commerce_controller['Center_images'].post('Center_image', response={
    201: ImageOut_C,
    400: MessageOut
})
def create_image(request, payload: ImageOut_C):
    try:
        img = Center_image.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, img

@commerce_controller['Center_images'].put('Center_image/{id}', response={200: update_Images_C})
def update_image(request, id: UUID4, payload: update_Images_C):
    updateimg = get_object_or_404(Center_image, id=id)
    for attr, value in payload.dict().items():
        setattr(updateimg, attr, value)
    updateimg.save()


@commerce_controller['Center_images'].delete('Center_image/{id}')
def delete_Images(request, id: UUID4):
    img = get_object_or_404(Center_image, id=id)
    img.delete()

##########################################################


@commerce_controller['Center'].get('Center', response={
    200: List[Center], })
def list_centers(request):
    ctr = center.objects.all()
    return ctr


@commerce_controller['Center'].post('center', response={
    201: CenterOut,
    400: MessageOut
})
def create_Center(request, payload: update_Center):
    try:
        ctr = center.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, ctr


@commerce_controller['Center'].get('center/{id}', response={
    200: CenterOut
})
def retrieve_center(request, id):
    return get_object_or_404(center, id=id)


@commerce_controller['Center'].put('center/{id}', response={200: update_Center})
def update_center(request, id: UUID4, payload: update_Center):
    updatectr = get_object_or_404(center, id=id)
    for attr, value in payload.dict().items():
        setattr(updatectr, attr, value)
    updatectr.save()


@commerce_controller['Center'].delete('center/{id}')
def delete_center(request, id: UUID4):
    ctr = get_object_or_404(center, id=id)
    ctr.delete()


@commerce_controller['Center'].get('Search', response={
    200: List[CenterOut],
})
def search_center(request, q: str = None,):
    center = Center.objects.all()

    if q:
        center = center.filter(
            Q(nameicontains=q) | Q(descriptionicontains=q)
        )

    """if price_lte:
        service = service.filter(discounted_pricelte=price_lte)

    if price_gte:
        service = service.filter(discounted_pricegte=price_gte)"""

    return center


####################################################


@commerce_controller['Advertising'].get('advertising', response={
    200: List[Advertising], })
def list_ads(request):
    ads = advertising.objects.all()
    return ads


@commerce_controller['Advertising'].post('advertising', response={
    201: AdvertisingOut,
    400: MessageOut
})
def create_ads(request, payload: update_Advertising):
    try:
        ads = advertising.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, ads


@commerce_controller['Advertising'].get('advertising/{id}', response={
    200: AdvertisingOut
})
def retrieve_ads(request, id):
    return get_object_or_404(advertising, id=id)


@commerce_controller['Advertising'].put('advertising/{id}', response={200: update_Advertising})
def update_ads(request, id: UUID4, payload: update_Advertising):
    updateads = get_object_or_404(advertising, id=id)
    for attr, value in payload.dict().items():
        setattr(updateads, attr, value)
    updateads.save()


@commerce_controller['Advertising'].delete('Advertising/{id}')
def delete_ads(request, id: UUID4):
    ads = get_object_or_404(advertising, id=id)
    ads.delete()




#######################################


@commerce_controller['News'].get('news', response={
    200: List[News], })
def list_news(request):
    nws = news.objects.all()
    return nws


@commerce_controller['News'].post('news', response={
    201: NewsOut,
    400: MessageOut
})
def create_news(request, payload: update_News):
    try:
        nws = news.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, nws


@commerce_controller['News'].get('news/{id}', response={
    200: NewsOut,
    400: MessageOut
})
def retrieve_news(request, id):
    return get_object_or_404(news, id=id)


@commerce_controller['News'].put('news/{id}', response={200: update_Advertising})
def update_news(request, id: UUID4, payload: update_News):
    updatenws = get_object_or_404(news, id=id)
    for attr, value in payload.dict().items():
        setattr(updatenws, attr, value)
    updatenws.save()


@commerce_controller['News'].delete('news/{id}')
def delete_news(request, id: UUID4):
    nws = get_object_or_404(news, id=id)
    nws.delete()
##################################

@commerce_controller['Center_opinions'].get('center_opinions', response={
    200: List[Center_opinion], })
def list_opinion(request):
    opn = Center_opinion.objects.all()
    return opn


@commerce_controller['Center_opinions'].post('center_opinions', response={
    201: Center_opinionOUT,
    400: MessageOut
})
def create_opinion(request, payload: Update_Center_opinion):
    try:
        opn = Center_opinion.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, opn


@commerce_controller['Center_opinions'].get('center_opinions/{id}', response={
    200: Center_opinionOUT,
    400: MessageOut
})
def retrieve_opinion(request, id):
    return get_object_or_404(Center_opinion, id=id)



@commerce_controller['Center_opinions'].get('center_opinions/')
def rate(request, r: float):
    while r>=0.0 and r<=5.0:
        return {"Rating": r}
    else: return "rating from 0 to 5"


##################################

@commerce_controller['Service_opinions'].get('service_opinions', response={
    200: List[Service_opinion], })
def list_opinion(request):
    opn = Service_opinion.objects.all()
    return opn


@commerce_controller['Service_opinions'].post('service_opinions', response={
    201: Service_opinionOUT,
    400: MessageOut
})
def create_opinion(request, payload: Update_Service_opinion):
    try:
        opn = Service_opinion.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, opn


@commerce_controller['Service_opinions'].get('service_opinions/{id}', response={
    200: Service_opinionOUT,
    400: MessageOut
})
def retrieve_opinion(request, id):
    return get_object_or_404(Service_opinion, id=id)



@commerce_controller['Service_opinions'].get('service_opinions/')
def rate(request, r: float):
    while r>=0.0 and r<=5.0:
        return {"Rating": r}
    else: return "rating from 0 to 5"

##########################################



@commerce_controller['Reservation'].get('reservation', response={
    200: List[Reservation], })
def list_reservation(request):
    rsv = reservation.objects.all()
    return rsv

@commerce_controller['Reservation'].post('reservation', response={
    201: ReservationOut,
    400: MessageOut
})
def create_reservation(request, payload: update_Reservation):
    try:
        rsv = reservation.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, rsv

@commerce_controller['Reservation'].put('reservation/{id}', response={200: update_Reservation})
def update_reservation(request, id: UUID4, payload: update_Reservation):
    updatersv = get_object_or_404(news, id=id)
    for attr, value in payload.dict().items():
        setattr(updatersv, attr, value)
    updatersv.save()

@commerce_controller['Reservation'].delete('reservation/{id}')
def delete_reservation(request, id: UUID4):
    rsv = get_object_or_404(reservation, id=id)
    rsv.delete()










'''
/api/resource/{id}/

/api/resource?id=&name=&age=

{
    JSON
}
'''

@commerce_controller['products'].get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


@commerce_controller['products'].post('products', response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product




# @commerce_controller.put('product/{id}')
# def update_product(request):
#     pass
#
#
# @commerce_controller.delete('product/{id}')
# def delete_product(request):
#     pass



@order_controller.post('add-to-cart', response=MessageOut)
def add_to_cart(request, payload: AddToCartPayload):
    payload_validated = payload.copy()
    if payload.qty < 1:
        payload_validated.qty = 1

    try:
        item = Item.objects.get(product_id=payload.product_id)
    except Item.DoesNotExist:
        Item.objects.create(product_id=payload.product_id, user=User.objects.first(), item_qty=payload_validated.qty,
                            ordered=False)
        return 200, {'detail': 'item added to cart successfully!'}

    item.item_qty += payload_validated.qty
    item.save()
    return 200, {'detail': 'item qty updated successfully!'}


@order_controller.post('increase-item/{item_id}', response=MessageOut)
def increase_item_qty(request, item_id: UUID4):
    item = get_object_or_404(Item, id=item_id, user=User.objects.first())
    item.item_qty += 1
    item.save()

    return 200, {'detail': 'Item qty increased successfully!'}


'''
* Decrease items qty
* Delete item from cart
* Create order
* Checkout

'''