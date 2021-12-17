import datetime

from ninja import Schema
from pydantic import UUID4
from django.contrib.auth import get_user_model

User=get_user_model()


class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str

class LabelOut(Schema):
    id: UUID4
    name: str

class notifications(Schema):
    id: UUID4
    title: str
    sender: str
    description: str
    time: datetime.time


class update_notifications(Schema):
    title: str
    sender: str
    description: str
    image: str
    time: datetime.time


class notificationsOut(Schema):
    id: UUID4
    title: str
    sender: str
    description: str
    image: str
    time: datetime.time

    ###########################################

class Service_opinion(Schema):
    id: UUID4
    # rating: float
    description: str
    #User.username
    time: datetime.time


class Service_opinionOUT(Schema):
    id: UUID4
    # rating: float
    description: str
    #User.username
    time: datetime.time


class Update_Service_opinion(Schema):
    #user: User
    # rating: float
    description: str
    time: datetime.time


########################################


class Image_S(Schema):

    id:UUID4
    #service_id:UUID4
    image:str


class ImageOut_S(Schema):
    id: UUID4
   # service_id:UUID4
    image:str

class update_Images_S(Schema):
    image:str


#########################################
class Services(Schema):
    id: UUID4
    name: str
    description: str
    time: datetime.time
    service_image:str
    price: float
    label_id:UUID4



class ServiceOut(Schema):
    id: UUID4
    name: str
    description: str
    time: datetime.time
    Service_images:list[ImageOut_S]
    Service_opinions:list[Update_Service_opinion]
    background_image:str
    price: float
    label: LabelOut


class update_Services(Schema):
    id: UUID4
    name: str
    description: str
    time: datetime.time
    service_image: str
    price: float


########################################


class Image_C(Schema):
    id:UUID4
    image:str


class ImageOut_C(Schema):
    id: UUID4
    image:str

class update_Images_C(Schema):
    image:str



#####################################


class Center_opinion(Schema):
    id: UUID4
    # rating: float
    description: str
    time: datetime.time


class Center_opinionOUT(Schema):
    id: UUID4
    # rating: float
    description: str
    time: datetime.time


class Update_Center_opinion(Schema):
    #user: User
    # rating: float
    description: str
    time: datetime.time







###################################

class Center(Schema):
    id: UUID4
    name: str
    description: str
    location: str
    image: str
    open_days: datetime.date
    close_days: datetime.date
    open_time: datetime.time
    close_time: datetime.time
    services: list[ServiceOut]
    Center_images: list[ImageOut_C]
    Center_opinions:list[Update_Center_opinion]




class CenterOut(Schema):
    id: UUID4
    name: str
    description: str
    location: str
    image: str
    open_time:  datetime.time
    close_time: datetime.time
    open_days: datetime.date
    close_days: datetime.date


class update_Center(Schema):
    name: str
    description: str
    location: str
    image: str
    open_time: datetime.time
    close_time:datetime.time
    open_days: datetime.date
    close_days:datetime.date


##################################################

class Advertising(Schema):
    id: UUID4
    name: str
    description: str
    center:CenterOut




class AdvertisingOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str


class update_Advertising(Schema):
    name: str
    description: str
    image: str
    center_id: UUID4


####################################
class News(Schema):
    id: UUID4
    title: str
    description: str
    # time: str


class NewsOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str
    # time: str


class update_News(Schema):
    title: str
    description: str
    image: str



############################3

class Reservation(Schema):
    id: UUID4
    title: str
    time: datetime.time
    is_active: bool



class ReservationOut(Schema):
    id: UUID4
    title: str
    time: datetime.time
    is_active: bool



class update_Reservation(Schema):
    title: str
    time: datetime.time
    is_active: bool


############################


class MerchantOut(Schema):
    id: UUID4
    name: str
    created: str
    updated: str

class VendorOut(Schema):
    id: UUID4
    name: str
    image: str


class ProductOut(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category: CategoryOut
    vendor: VendorOut
    merchant: MerchantOut
    label: LabelOut
    created: str
    updated: str

class ProductCreate(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int
    category_id: UUID4
    vendor_id: UUID4
    merchant_id: UUID4
    label_id: UUID4


class AddToCartPayload(Schema):
    product_id: UUID4
    qty: int

