# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class BusinessRoleRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessRoleRequest = True
        super(BusinessRoleRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        created_by = 'created_by'
        created_time = 'created_time'
        email = 'email'
        expiration_time = 'expiration_time'
        expiry_time = 'expiry_time'
        finance_role = 'finance_role'
        id = 'id'
        invite_link = 'invite_link'
        ip_role = 'ip_role'
        owner = 'owner'
        role = 'role'
        status = 'status'
        updated_by = 'updated_by'
        updated_time = 'updated_time'

    class Role:
        finance_editor = 'FINANCE_EDITOR'
        finance_analyst = 'FINANCE_ANALYST'
        ads_rights_reviewer = 'ADS_RIGHTS_REVIEWER'
        admin = 'ADMIN'
        employee = 'EMPLOYEE'
        fb_employee_sales_rep = 'FB_EMPLOYEE_SALES_REP'

    class Status:
        pending = 'PENDING'
        accepted = 'ACCEPTED'
        declined = 'DECLINED'
        expired = 'EXPIRED'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRoleRequest,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'role': 'role_enum',
        }
        enums = {
            'role_enum': BusinessRoleRequest.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRoleRequest,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_client_assets(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'asset_type': 'asset_type_enum',
        }
        enums = {
            'asset_type_enum': [
                'PAGE',
                'AD_ACCOUNT',
                'PRODUCT_CATALOG',
                'APP',
                'PIXEL',
                'SYSTEM_USER',
                'BRAND',
                'USER',
                'PROJECT',
                'INSTAGRAM_ACCOUNT',
                'ATLAS_ADVERTISER',
                'FUNDING_SOURCE',
                'LEGACY_LOGIN',
                'BUSINESS_REQUEST',
                'EXAMPLE_CAT',
                'MONETIZATION_PROPERTY',
                'GRP_PLAN',
                'PERSONA',
                'CREDIT_PARTITION',
                'PAYOUT_ACCOUNT',
                'AD_STUDY',
                'SAVED_AUDIENCE',
                'CUSTOM_AUDIENCE',
                'PLATFORM_CUSTOM_AUDIENCE',
                'EVENT_SOURCE_GROUP',
                'OFFLINE_CONVERSION_DATA_SET',
                'AD_IMAGE',
                'PHOTO',
                'BLOCK_LIST',
                'FINANCE',
                'IP',
                'CREDIT_PARTITION_CONFIG',
                'VIDEO_ASSET',
                'BUSINESS_UNIT',
                'PAGE_FOR_LOCATIONS',
                'AD_ACCOUNT_CREATION_REQUEST',
                'RESELLER_VETTING_OE_REQUEST',
                'REGISTERED_TRADEMARK',
                'CUSTOM_CONVERSION',
                'LEADS_ACCESS',
                'SPACO_DS_DATA_COLLECTION',
                'OWNED_DOMAIN',
                'WHATSAPP_BUSINESS_ACCOUNT',
                'BUSINESS_RESOURCE_GROUP',
                'HOTEL_PRICE_FETCHER_PULL_CONFIG',
                'NEWS_PAGE',
                'PLACE_PAGE_SET',
                'BUSINESS_LOCATIONS_WRAPPER',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_client_assets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_owned_assets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessobject import BusinessObject
        param_types = {
            'asset_type': 'asset_type_enum',
        }
        enums = {
            'asset_type_enum': BusinessObject.AssetType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_owned_assets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'created_by': 'Object',
        'created_time': 'datetime',
        'email': 'string',
        'expiration_time': 'datetime',
        'expiry_time': 'datetime',
        'finance_role': 'string',
        'id': 'string',
        'invite_link': 'string',
        'ip_role': 'string',
        'owner': 'Business',
        'role': 'string',
        'status': 'string',
        'updated_by': 'Object',
        'updated_time': 'datetime',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Role'] = BusinessRoleRequest.Role.__dict__.values()
        field_enum_info['Status'] = BusinessRoleRequest.Status.__dict__.values()
        return field_enum_info