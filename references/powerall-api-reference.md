# Powerall Connect API Reference

**Base URL:** `https://connect.powerall.io`
**Auth:** Basic Authentication (tenant name + API token)
**Format:** JSON
**Swagger Version:** 2.0

## Overview

The Powerall Connect API allows you to get data from your Powerall Connect administration, as well as to do some modifications to it.

- The API is mostly RESTful, except for some specific flows like creating product stock corrections, which is a POST with a special verb.
- Flexible filters on all fields.
- Include system to lower the number of requests needed.
- All decimal values are wrapped in strings to prevent unintended loss of precision.

## Authentication

A username and password are required. The username is unique per Powerall Connect administration. The password is a token with the corresponding permissions. Authentication is via Basic Authentication (Authorization header).

Are you looking for credentials? Contact your Powerall supplier.

---


## ContactPerson

### GET `/v1/contact-persons`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ContactPersonContractListResponseWrapperContract](#model-contactpersoncontractlistresponsewrappercontract)

---

### POST `/v1/contact-persons`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses relations.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateContactPersonContract | No |  |

**Request body:** [CreateContactPersonContract](#model-createcontactpersoncontract)

**Responses:**

- `200` OK -> [ContactPersonContractResponseWrapperContract](#model-contactpersoncontractresponsewrappercontract)

---

### PUT `/v1/contact-persons/{id}`

relations.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| body | body | EditContactPersonContract | No |  |

**Request body:** [EditContactPersonContract](#model-editcontactpersoncontract)

**Responses:**

- `200` OK

---

### DELETE `/v1/contact-persons/{id}`

relations.delete

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |

**Responses:**

- `200` OK

---


## Contract

### GET `/v1/contracts`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses InvoiceRelation Country VatInformation VatInformation DeliveryAddresses Seller Lines ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Contract Relation Country VatInformation VatInformation DeliveryAddresses Seller contracts.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ContractContractListResponseWrapperContract](#model-contractcontractlistresponsewrappercontract)

---

### GET `/v1/contracts/lines`

Possible includes: ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Contract Relation Country VatInformation VatInformation DeliveryAddresses Seller Lines ServiceObject ConfigurationElements Product Suppliers Structure Lines Translations Groups Product Suppliers Structure Lines Translations WebsiteInformation contracts.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ContractLineContractListResponseWrapperContract](#model-contractlinecontractlistresponsewrappercontract)

---


## CostCenter

### GET `/v1/cost-centers`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [CostCenterContractListResponseWrapperContract](#model-costcentercontractlistresponsewrappercontract)

---


## Country

### GET `/v1/countries`

Possible includes: VatInformation Language basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [CountryContractListResponseWrapperContract](#model-countrycontractlistresponsewrappercontract)

---


## Deliveries

### GET `/v1/deliveries`

Possible includes: PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Parcels Items Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Delivery PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country DeliveryAddresses SalesOrder Country Relation Country DeliveryAddresses Relation Country VatInformation VatInformation DeliveryAddresses DeliveryCondition salesorders.read or deliveries.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [DeliveryContractListResponseWrapperContract](#model-deliverycontractlistresponsewrappercontract)

---

### POST `/v1/deliveries`

deliveries.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | CreateDeliveryContract | No |  |

**Request body:** [CreateDeliveryContract](#model-createdeliverycontract)

**Responses:**

- `200` OK

---

### GET `/v1/deliveries/{deliveryNumber}`

Possible includes: PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Parcels Items Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Delivery PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country DeliveryAddresses SalesOrder Country Relation Country DeliveryAddresses Relation Country VatInformation VatInformation DeliveryAddresses DeliveryCondition salesorders.read or deliveries.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| deliveryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [DeliveryContractResponseWrapperContract](#model-deliverycontractresponsewrappercontract)

---


## DeliveryAddress

### GET `/v1/relations/{idOrCode}/delivery-addresses`

Possible includes: Country VatInformation DeliveryCondition relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [DeliveryAddressContractListResponseWrapperContract](#model-deliveryaddresscontractlistresponsewrappercontract)

---

### POST `/v1/relations/{idOrCode}/delivery-addresses`

Possible includes: Country VatInformation DeliveryCondition deliveryaddresses.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| include | query | string | No |  |
| body | body | CreateDeliveryAddressContract | No |  |

**Request body:** [CreateDeliveryAddressContract](#model-createdeliveryaddresscontract)

**Responses:**

- `200` OK -> [DeliveryAddressContractResponseWrapperContract](#model-deliveryaddresscontractresponsewrappercontract)

---

### GET `/v1/relations/{idOrCode}/delivery-addresses/{id}`

Possible includes: Country VatInformation DeliveryCondition relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| idOrCode | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [DeliveryAddressContractResponseWrapperContract](#model-deliveryaddresscontractresponsewrappercontract)

---

### PUT `/v1/relations/{idOrCode}/delivery-addresses/{id}`

deliveryaddresses.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| id | path | string | Yes |  |
| body | body | EditDeliveryAddressContract | No |  |

**Request body:** [EditDeliveryAddressContract](#model-editdeliveryaddresscontract)

**Responses:**

- `200` OK

---

### DELETE `/v1/relations/{idOrCode}/delivery-addresses/{id}`

deliveryaddresses.delete

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| id | path | string | Yes |  |

**Responses:**

- `200` OK

---


## DeliveryCondition

### GET `/v1/delivery-conditions`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [DeliveryConditionContractListResponseWrapperContract](#model-deliveryconditioncontractlistresponsewrappercontract)

---


## Employee

### GET `/v1/employees`

employees.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [EmployeeContractListResponseWrapperContract](#model-employeecontractlistresponsewrappercontract)

---


## File

### POST `/v1/files`

**Responses:**

- `200` OK -> [FileIdContractResponseWrapperContract](#model-fileidcontractresponsewrappercontract)

---


## GeneralLedgerAccount

### GET `/v1/general-ledger-accounts`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [GeneralLedgerAccountContractListResponseWrapperContract](#model-generalledgeraccountcontractlistresponsewrappercontract)

---


## GoodsReceipt

### GET `/v1/goods-receipts/expected`

Possible includes: Supplier Country VatInformation VatInformation DeliveryAddresses Warehouse Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations PurchaseOrderLine SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse PurchaseOrder Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ExpectedGoodsReceiptContractResponseWrapperContract](#model-expectedgoodsreceiptcontractresponsewrappercontract)

---

### GET `/v1/goods-receipts/expected/{entryNumber}`

Possible includes: Supplier Country VatInformation VatInformation DeliveryAddresses Warehouse Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations PurchaseOrderLine SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse PurchaseOrder Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| entryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ExpectedGoodsReceiptContractResponseWrapperContract](#model-expectedgoodsreceiptcontractresponsewrappercontract)

---

### POST `/v1/goods-receipts/expected/{entryNumber}/receive`

products.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| entryNumber | path | integer | Yes |  |
| body | body | ExpectedGoodsReceiptBookingContract | No |  |

**Request body:** [ExpectedGoodsReceiptBookingContract](#model-expectedgoodsreceiptbookingcontract)

**Responses:**

- `200` OK

---


## Invoices

### GET `/v1/invoices`

Possible includes: PreInvoices Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Relation Country VatInformation VatInformation DeliveryAddresses invoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [InvoiceContractListResponseWrapperContract](#model-invoicecontractlistresponsewrappercontract)

---

### GET `/v1/invoices/{relationCode}:{invoiceNumber}`

Possible includes: PreInvoices Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Relation Country VatInformation VatInformation DeliveryAddresses invoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| invoiceNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [InvoiceContractResponseWrapperContract](#model-invoicecontractresponsewrappercontract)

---


## Journal

### GET `/v1/journals`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |

**Responses:**

- `200` OK -> [JournalContractListResponseWrapperContract](#model-journalcontractlistresponsewrappercontract)

---

### POST `/v1/journals/{journalId}/entries`

journalentries.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| journalId | path | integer | Yes |  |
| body | body | CreateJournalEntryContract | No |  |

**Request body:** [CreateJournalEntryContract](#model-createjournalentrycontract)

**Responses:**

- `200` OK -> [IdContractResponseWrapperContract](#model-idcontractresponsewrappercontract)

---


## Last modified rules

### GET `/v1/last-modified-rules`

lastmodifiedrules.read

**Responses:**

- `200` OK -> [LastModifiedRuleContractListResponseWrapperContract](#model-lastmodifiedrulecontractlistresponsewrappercontract)

---

### POST `/v1/last-modified-rules`

lastmodifiedrules.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | CreateLastModifiedRuleContract | No |  |

**Request body:** [CreateLastModifiedRuleContract](#model-createlastmodifiedrulecontract)

**Responses:**

- `200` OK -> [LastModifiedRuleContractResponseWrapperContract](#model-lastmodifiedrulecontractresponsewrappercontract)

---

### PUT `/v1/last-modified-rules/{entity}`

lastmodifiedrules.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| entity | path |  | Yes |  |
| body | body | EditLastModifiedRuleContract | No |  |

**Request body:** [EditLastModifiedRuleContract](#model-editlastmodifiedrulecontract)

**Responses:**

- `200` OK -> [LastModifiedRuleContractResponseWrapperContract](#model-lastmodifiedrulecontractresponsewrappercontract)

---

### DELETE `/v1/last-modified-rules/{entity}`

lastmodifiedrules.delete

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| entity | path |  | Yes |  |

**Responses:**

- `200` OK

---


## Parcel

### GET `/v1/parcels`

Possible includes: Items Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Delivery PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country DeliveryAddresses SalesOrder Country Parcels Items Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations Relation Country DeliveryAddresses deliveries.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ParcelContractListResponseWrapperContract](#model-parcelcontractlistresponsewrappercontract)

---


## PaymentCondition

### GET `/v1/payment-conditions`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [PaymentConditionContractListResponseWrapperContract](#model-paymentconditioncontractlistresponsewrappercontract)

---


## Permission

### GET `/v1/permissions`

**Responses:**

- `200` OK -> [PermissionContractListResponseWrapperContract](#model-permissioncontractlistresponsewrappercontract)

---

### GET `/v1/permissions/all`

**Responses:**

- `200` OK

---


## Picklist

### GET `/v1/pick-lists`

Possible includes: Lines ParcelItem picklists.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filter | query |  | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PicklistContractListResponseWrapperContract](#model-picklistcontractlistresponsewrappercontract)

---


## PreInvoice

### GET `/v1/pre-invoices`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours PreInvoice SalesOrder Lines Product Suppliers Structure Lines Translations DeliveryLines Delivery Lines Product Suppliers Structure Lines Translations SalesOrderLine Parcels Items Product Suppliers Structure Lines Translations Invoice Lines SalesOrderLine Product Suppliers Structure Lines Translations DeliveryLines Product Suppliers Structure Lines Translations Delivery PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country DeliveryAddresses SalesOrder Country Parcels Items Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations Relation Country DeliveryAddresses Invoice PreInvoices Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Relation Country VatInformation VatInformation DeliveryAddresses PaymentCondition DeliveryCondition Lines SalesOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines WorkOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse Warehouse Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller invoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PreInvoiceContractListResponseWrapperContract](#model-preinvoicecontractlistresponsewrappercontract)

---

### GET `/v1/pre-invoices/{relationCode}:{entryNumber}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours PreInvoice SalesOrder Lines Product Suppliers Structure Lines Translations DeliveryLines Delivery Lines Product Suppliers Structure Lines Translations SalesOrderLine Parcels Items Product Suppliers Structure Lines Translations Invoice Lines SalesOrderLine Product Suppliers Structure Lines Translations DeliveryLines Product Suppliers Structure Lines Translations Delivery PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Employee Lines Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country DeliveryAddresses SalesOrder Country Parcels Items Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations Relation Country DeliveryAddresses Invoice PreInvoices Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations Relation Country VatInformation VatInformation DeliveryAddresses PaymentCondition DeliveryCondition Lines SalesOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines WorkOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse Warehouse Product Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller invoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PreInvoiceContractResponseWrapperContract](#model-preinvoicecontractresponsewrappercontract)

---


## Product

### GET `/v1/products`

Possible includes: Stock Make Suppliers Relation Country VatInformation VatInformation DeliveryAddresses DossierItems Properties GroupDescriptions Structure Lines Product Stock Suppliers Relation Country DeliveryAddresses Translations FinancialGroupDescription SelectionCodeDescriptions Translations IncludeObject products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductContractListResponseWrapperContract](#model-productcontractlistresponsewrappercontract)

---

### GET `/v1/products/export.{returnType}`

Possible includes: Stock Make Suppliers Relation Country VatInformation VatInformation DeliveryAddresses DossierItems Properties GroupDescriptions Structure Lines Product Stock Suppliers Relation Country DeliveryAddresses Translations FinancialGroupDescription SelectionCodeDescriptions Translations IncludeObject products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| include | query | string | No |  |
| returnType | path | string | Yes |  |

**Responses:**

- `200` OK -> [ProductContractListResponseWrapperContract](#model-productcontractlistresponsewrappercontract)

---

### GET `/v1/products/mutations`

Possible includes: Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse DestinationWarehouse ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductMutationContractListResponseWrapperContract](#model-productmutationcontractlistresponsewrappercontract)

---

### POST `/v1/products/prices`

products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | PriceRequestContract | No |  |

**Request body:** [PriceRequestContract](#model-pricerequestcontract)

**Responses:**

- `200` OK -> [ProductPriceContractListResponseWrapperContract](#model-productpricecontractlistresponsewrappercontract)

---

### POST `/v1/products/stock-corrections`

products.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | ProductStockCorrectionContract | No |  |

**Request body:** [ProductStockCorrectionContract](#model-productstockcorrectioncontract)

**Responses:**

- `200` OK

---

### GET `/v1/products/{productCode}`

Possible includes: Stock Make Suppliers Relation Country VatInformation VatInformation DeliveryAddresses DossierItems Properties GroupDescriptions Structure Lines Product Stock Suppliers Relation Country DeliveryAddresses Translations FinancialGroupDescription SelectionCodeDescriptions Translations IncludeObject products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| productCode | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductContractResponseWrapperContract](#model-productcontractresponsewrappercontract)

---

### PATCH `/v1/products/{productCode}`

products.update Description1 (string) FinancialGroup (integer) MainGroup (string) SubGroup (string) SalesPriceUnit (string) SalesPriceQuantity (integer) SalesUnit (string) SalesQuantity (integer) SearchName (string) EanCode (string) Weight (number) EquivalentCode (string) Status (Active|Discontinued|NoLongerAvailable|OnRequest) SalesPrice (number) AdvicePrice (number) FactorTransferPriceSalesPrice (number) FactorSalesPriceAdvicePrice (number) TransferPrice (number) CbsCode (string) OriginCountryIsoCode (string)

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| productCode | path | string | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [KeyValueContract](#keyvaluecontract)

**Responses:**

- `200` OK

---

### POST `/v1/products/{productCode}/dossier-items`

products.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| productCode | path | string | Yes |  |
| body | body | AddFileContract | No |  |

**Request body:** [AddFileContract](#model-addfilecontract)

**Responses:**

- `200` OK

---


## ProductGroup

### GET `/v1/product-groups`

products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [ProductGroupContractFlatListResponseWrapperContract](#model-productgroupcontractflatlistresponsewrappercontract)

---


## ProductMake

### GET `/v1/product-makes`

Possible includes: Stock Make Suppliers Relation Country VatInformation VatInformation DeliveryAddresses DossierItems Properties GroupDescriptions Structure Lines Product Stock Suppliers Relation Country DeliveryAddresses Translations FinancialGroupDescription SelectionCodeDescriptions Translations IncludeObject products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductMakeContractListResponseWrapperContract](#model-productmakecontractlistresponsewrappercontract)

---


## ProductSupplier

### GET `/v1/products/{productCode}/suppliers/{relationCode}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| productCode | path | string | Yes |  |
| relationCode | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductContractResponseWrapperContract](#model-productcontractresponsewrappercontract)

---

### PATCH `/v1/products/{productCode}/suppliers/{relationCode}`

products.update PurchaseProductCode (string) PurchaseCatalogCode (string) MainGroup (string) SubGroup (string) MakeCode (string) PurchaseUnit (string) PurchaseQuantity (integer) PurchasePriceUnit (string) PurchasePriceQuantity (integer) StockQuantityPerUnit (number) OrderQuantity (integer) PurchasePrice (number) SalesPrice (number) EanCode (string)

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| productCode | path | string | Yes |  |
| relationCode | path | integer | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [KeyValueContract](#keyvaluecontract)

**Responses:**

- `200` OK

---


## PurchaseInvoice

### GET `/v1/purchase-invoices`

purchaseinvoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |

**Responses:**

- `200` OK -> [PurchaseInvoiceContractListResponseWrapperContract](#model-purchaseinvoicecontractlistresponsewrappercontract)

---

### POST `/v1/purchase-invoices`

purchaseinvoices.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body | CreatePurchaseInvoiceContract | No |  |

**Request body:** [CreatePurchaseInvoiceContract](#model-createpurchaseinvoicecontract)

**Responses:**

- `200` OK -> [IdContractResponseWrapperContract](#model-idcontractresponsewrappercontract)

---

### GET `/v1/purchase-invoices/{id}`

purchaseinvoices.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |

**Responses:**

- `200` OK -> [PurchaseInvoiceContractResponseWrapperContract](#model-purchaseinvoicecontractresponsewrappercontract)

---

### POST `/v1/purchase-invoices/{id}/approve`

purchaseinvoices.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| body | body | PurchaseInvoiceApproveContract | No |  |

**Request body:** [PurchaseInvoiceApproveContract](#model-purchaseinvoiceapprovecontract)

**Responses:**

- `200` OK

---

### POST `/v1/purchase-invoices/{id}/fiat`

purchaseinvoices.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| body | body | PurchaseInvoiceFiatContract | No |  |

**Request body:** [PurchaseInvoiceFiatContract](#model-purchaseinvoicefiatcontract)

**Responses:**

- `200` OK

---

### POST `/v1/purchase-invoices/{id}/register-matching-receipts`

purchaseinvoices.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [ProductMutationMatchContract](#productmutationmatchcontract)

**Responses:**

- `200` OK

---


## PurchaseOrder

### GET `/v1/purchase-orders`

Possible includes: Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse PurchaseOrder Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry VatInformation DeliveryCountry VatInformation purchaseorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PurchaseOrderContractListResponseWrapperContract](#model-purchaseordercontractlistresponsewrappercontract)

---

### GET `/v1/purchase-orders/lines`

Possible includes: Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines WorkOrderLine Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse PurchaseOrder Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry purchaseorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PurchaseOrderLineContractListResponseWrapperContract](#model-purchaseorderlinecontractlistresponsewrappercontract)

---

### GET `/v1/purchase-orders/{id}`

Possible includes: Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse PurchaseOrder Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry VatInformation DeliveryCountry VatInformation purchaseorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PurchaseOrderContractResponseWrapperContract](#model-purchaseordercontractresponsewrappercontract)

---

### GET `/v1/purchase-orders/{relationCode}:{entryNumber}`

Possible includes: Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses DeliveryLines WorkOrderLine Warehouse PurchaseOrder Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry Relation Country VatInformation VatInformation DeliveryAddresses Warehouse InvoiceCountry VatInformation DeliveryCountry VatInformation purchaseorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [PurchaseOrderContractResponseWrapperContract](#model-purchaseordercontractresponsewrappercontract)

---


## Quotation

### POST `/v1/quotations/{relationCode}:{entryNumber}/confirm`

quotations.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [AddFileContract](#addfilecontract)

**Responses:**

- `200` OK

---

### POST `/v1/quotations/{relationCode}:{entryNumber}/reject`

quotations.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [AddFileContract](#addfilecontract)

**Responses:**

- `200` OK

---


## Relation

### GET `/v1/relations`

Possible includes: Country VatInformation VatInformation DeliveryCondition PaymentCondition Currency DeliveryAddresses Country VatInformation DeliveryCondition EDocumentEmailAddresses ContactPersons relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [RelationContractListResponseWrapperContract](#model-relationcontractlistresponsewrappercontract)

---

### POST `/v1/relations`

Possible includes: Country VatInformation VatInformation DeliveryCondition PaymentCondition Currency DeliveryAddresses Country VatInformation DeliveryCondition EDocumentEmailAddresses ContactPersons relations.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateRelationContract | No |  |

**Request body:** [CreateRelationContract](#model-createrelationcontract)

**Responses:**

- `200` OK -> [RelationContractResponseWrapperContract](#model-relationcontractresponsewrappercontract)

---

### GET `/v1/relations/export.{returnType}`

Possible includes: Country VatInformation VatInformation DeliveryCondition PaymentCondition Currency DeliveryAddresses Country VatInformation DeliveryCondition EDocumentEmailAddresses ContactPersons relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| include | query | string | No |  |
| returnType | path | string | Yes |  |

**Responses:**

- `200` OK -> [RelationContractListResponseWrapperContract](#model-relationcontractlistresponsewrappercontract)

---

### GET `/v1/relations/{idOrCode}`

Possible includes: Country VatInformation VatInformation DeliveryCondition PaymentCondition Currency DeliveryAddresses Country VatInformation DeliveryCondition EDocumentEmailAddresses ContactPersons relations.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [RelationContractResponseWrapperContract](#model-relationcontractresponsewrappercontract)

---

### PUT `/v1/relations/{idOrCode}`

Possible includes: Country VatInformation VatInformation DeliveryCondition PaymentCondition Currency DeliveryAddresses Country VatInformation DeliveryCondition EDocumentEmailAddresses ContactPersons relations.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrCode | path | string | Yes |  |
| include | query | string | No |  |
| body | body | EditRelationContract | No |  |

**Request body:** [EditRelationContract](#model-editrelationcontract)

**Responses:**

- `200` OK -> [RelationContractResponseWrapperContract](#model-relationcontractresponsewrappercontract)

---


## SalesOrder

### GET `/v1/sales-orders`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses Seller Country VatInformation TotalPrices Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines DeliveryCondition PaymentCondition salesorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [SalesOrderContractListResponseWrapperContract](#model-salesordercontractlistresponsewrappercontract)

---

### POST `/v1/sales-orders`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses Seller Country VatInformation TotalPrices Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines DeliveryCondition PaymentCondition salesorders.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateSalesOrderContract | No |  |

**Request body:** [CreateSalesOrderContract](#model-createsalesordercontract)

**Responses:**

- `200` OK -> [SalesOrderContractResponseWrapperContract](#model-salesordercontractresponsewrappercontract)

---

### GET `/v1/sales-orders/lines`

Possible includes: Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Relation Country VatInformation VatInformation DeliveryAddresses Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines DeliveryLines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country salesorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [SalesOrderLineContractListResponseWrapperContract](#model-salesorderlinecontractlistresponsewrappercontract)

---

### POST `/v1/sales-orders/lines/allocate`

salesorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body |  | No |  |

**Request body:**
Array of:
- [AllocateSalesOrderLineContract](#allocatesalesorderlinecontract)

**Responses:**

- `200` OK

---

### POST `/v1/sales-orders/lines/pick`

salesorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| body | body |  | No |  |

**Request body:**
Array of:
- [PickSalesOrderLineContract](#picksalesorderlinecontract)

**Responses:**

- `200` OK

---

### PATCH `/v1/sales-orders/lines/{idOrRecordNumber}`

salesorders.update QuantityAllocated (number)

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| idOrRecordNumber | path | string | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [KeyValueContract](#keyvaluecontract)

**Responses:**

- `200` OK

---

### POST `/v1/sales-orders/simulate`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses Seller Country VatInformation TotalPrices Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines DeliveryCondition PaymentCondition salesorders.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateSalesOrderContract | No |  |

**Request body:** [CreateSalesOrderContract](#model-createsalesordercontract)

**Responses:**

- `200` OK -> [SalesOrderContractResponseWrapperContract](#model-salesordercontractresponsewrappercontract)

---

### GET `/v1/sales-orders/{id}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses Seller Country VatInformation TotalPrices Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines DeliveryCondition PaymentCondition salesorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [SalesOrderContractResponseWrapperContract](#model-salesordercontractresponsewrappercontract)

---

### GET `/v1/sales-orders/{relationCode}:{entryNumber}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses Seller Country VatInformation TotalPrices Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations ServiceObject ConfigurationElements Seller SalesRelation Country DeliveryAddresses Groups WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country DeliveryLines DeliveryCondition PaymentCondition salesorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [SalesOrderContractResponseWrapperContract](#model-salesordercontractresponsewrappercontract)

---

### POST `/v1/sales-orders/{relationCode}:{entryNumber}/dossier-items`

salesorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| body | body | AddFileContract | No |  |

**Request body:** [AddFileContract](#model-addfilecontract)

**Responses:**

- `200` OK

---


## ServiceMessage

### GET `/v1/service-messages`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses servicemessages.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceMessageContractListResponseWrapperContract](#model-servicemessagecontractlistresponsewrappercontract)

---

### POST `/v1/service-messages`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses servicemessages.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateServiceMessageContract | No |  |

**Request body:** [CreateServiceMessageContract](#model-createservicemessagecontract)

**Responses:**

- `200` OK -> [ServiceMessageContractResponseWrapperContract](#model-servicemessagecontractresponsewrappercontract)

---

### POST `/v1/service-messages/drafts`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses servicemessages.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| include | query | string | No |  |
| body | body | CreateServiceMessageContract | No |  |

**Request body:** [CreateServiceMessageContract](#model-createservicemessagecontract)

**Responses:**

- `200` OK -> [ServiceMessageContractResponseWrapperContract](#model-servicemessagecontractresponsewrappercontract)

---

### PUT `/v1/service-messages/drafts/{id}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses servicemessages.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| include | query | string | No |  |
| body | body | EditServiceMessageContract | No |  |

**Request body:** [EditServiceMessageContract](#model-editservicemessagecontract)

**Responses:**

- `200` OK -> [ServiceMessageContractResponseWrapperContract](#model-servicemessagecontractresponsewrappercontract)

---

### DELETE `/v1/service-messages/drafts/{id}`

servicemessages.delete

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |

**Responses:**

- `200` OK

---

### POST `/v1/service-messages/drafts/{id}/submit`

servicemessages.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |

**Responses:**

- `200` OK -> [ServiceMessageContractResponseWrapperContract](#model-servicemessagecontractresponsewrappercontract)

---

### GET `/v1/service-messages/{id}`

Possible includes: Relation Country VatInformation VatInformation DeliveryAddresses servicemessages.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceMessageContractResponseWrapperContract](#model-servicemessagecontractresponsewrappercontract)

---


## ServiceMessageCategory

### GET `/v1/service-message-categories`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [ServiceMessageCategoryContractListResponseWrapperContract](#model-servicemessagecategorycontractlistresponsewrappercontract)

---


## ServiceObject

### GET `/v1/service-objects`

Possible includes: ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country VatInformation VatInformation DeliveryAddresses UserRelation Country VatInformation VatInformation DeliveryAddresses PurchaseRelation Country VatInformation VatInformation DeliveryAddresses Groups StandardGroup Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations DossierItems WebsiteInformation IncludeObject StickerNumbers serviceobjects.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectContractListResponseWrapperContract](#model-serviceobjectcontractlistresponsewrappercontract)

---

### GET `/v1/service-objects/{serviceNumber}`

Possible includes: ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country VatInformation VatInformation DeliveryAddresses UserRelation Country VatInformation VatInformation DeliveryAddresses PurchaseRelation Country VatInformation VatInformation DeliveryAddresses Groups StandardGroup Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations DossierItems WebsiteInformation IncludeObject StickerNumbers serviceobjects.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| serviceNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectContractResponseWrapperContract](#model-serviceobjectcontractresponsewrappercontract)

---

### PATCH `/v1/service-objects/{serviceNumber}`

serviceobjects.update MainGroupCode (string) SubGroupCode (string) FinancialGroup (integer) BuildYear (integer) Type (string) ProductCode (string) RegistrationNumber (string) MakeCode (integer) Description1 (string) Description2 (string) Description3 (string) Description4 (string) Description5 (string) Description6 (string) SerialNumber1 (string) SerialNumber2 (string) SerialNumber3 (string) WarrantyHours (integer) Inspection1StickerNumber (string) Inspection1LastDate (yyyy-MM-dd) Inspection1NextDate (yyyy-MM-dd) Inspection2StickerNumber (string) Inspection2LastDate (yyyy-MM-dd) Inspection2NextDate (yyyy-MM-dd) Inspection3StickerNumber (string) Inspection3LastDate (yyyy-MM-dd) Inspection3NextDate (yyyy-MM-dd) Inspection4StickerNumber (string) Inspection4LastDate (yyyy-MM-dd) Inspection4NextDate (yyyy-MM-dd) Counter1 (integer) InUseDate (yyyy-MM-dd) WarrantyDate (yyyy-MM-dd) CustomerRegCode (string)

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| serviceNumber | path | integer | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [KeyValueContract](#keyvaluecontract)

**Responses:**

- `200` OK

---

### POST `/v1/service-objects/{serviceNumber}/dossier-items`

serviceobjects.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| serviceNumber | path | integer | Yes |  |
| body | body |  | No |  |

**Request body:**
Array of:
- [AddFileContract](#addfilecontract)

**Responses:**

- `200` OK

---

### DELETE `/v1/service-objects/{serviceNumber}/dossier-items/{fileName}`

serviceobjects.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| serviceNumber | path | integer | Yes |  |
| fileName | path | string | Yes |  |

**Responses:**

- `200` OK

---

### POST `/v1/service-objects/{serviceNumber}/send-label`

serviceobjectlabel.create

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| serviceNumber | path | integer | Yes |  |
| body | body | ServiceObjectLabelSendRequestContract | No |  |

**Request body:** [ServiceObjectLabelSendRequestContract](#model-serviceobjectlabelsendrequestcontract)

**Responses:**

- `200` OK -> [ServiceObjectContractResponseWrapperContract](#model-serviceobjectcontractresponsewrappercontract)

---


## ServiceObjectGroup

### GET `/v1/service-object-groups`

Possible includes: StandardGroup serviceobjects.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectGroupContractListResponseWrapperContract](#model-serviceobjectgroupcontractlistresponsewrappercontract)

---


## ServiceObjectType

### GET `/v1/addons/service-objects/types`

Possible includes: PromotionalInformation serviceobjecttypes.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectTypeContractListResponseWrapperContract](#model-serviceobjecttypecontractlistresponsewrappercontract)

---

### GET `/v1/addons/service-objects/types/products/links/export.{returnType}`

serviceobjecttypes.read or products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| returnType | path | string | Yes |  |

**Responses:**

- `200` OK -> [ServiceObjectTypeProductSlugLinkContractListResponseWrapperContract](#model-serviceobjecttypeproductsluglinkcontractlistresponsewrappercontract)

---

### GET `/v1/addons/service-objects/types/suggestions`

serviceobjecttypes.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| make | query | string | No |  |
| model | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectTypeSuggestionContractListResponseWrapperContract](#model-serviceobjecttypesuggestioncontractlistresponsewrappercontract)

---

### GET `/v1/addons/service-objects/types/{make}/{model}/{year}`

Possible includes: PromotionalInformation serviceobjecttypes.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| make | path | string | Yes |  |
| model | path | string | Yes |  |
| year | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ServiceObjectTypeContractResponseWrapperContract](#model-serviceobjecttypecontractresponsewrappercontract)

---

### GET `/v1/addons/service-objects/types/{make}/{model}/{year}/products`

Possible includes: Stock Make Suppliers Relation Country VatInformation VatInformation DeliveryAddresses DossierItems Properties GroupDescriptions Structure Lines Product Stock Suppliers Relation Country DeliveryAddresses Translations FinancialGroupDescription SelectionCodeDescriptions Translations IncludeObject serviceobjecttypes.read or products.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| make | path | string | Yes |  |
| model | path | string | Yes |  |
| year | path | integer | Yes |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [ProductContractListResponseWrapperContract](#model-productcontractlistresponsewrappercontract)

---


## SyncAction

### GET `/v1/syncactions`

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [SyncActionContractResponseWrapperContract](#model-syncactioncontractresponsewrappercontract)

---

### GET `/v1/syncactions/{id}`

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | path | string | Yes |  |

**Responses:**

- `200` OK -> [SyncActionContractResponseWrapperContract](#model-syncactioncontractresponsewrappercontract)

---


## TaskType

### GET `/v1/task-types`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [TaskTypeContractListResponseWrapperContract](#model-tasktypecontractlistresponsewrappercontract)

---


## Vat codes

### GET `/v1/vat-codes`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |

**Responses:**

- `200` OK -> [VatCodeContractListResponseWrapperContract](#model-vatcodecontractlistresponsewrappercontract)

---


## Warehouse

### GET `/v1/warehouses`

basicinfo.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| filters | query | string | No |  |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |

**Responses:**

- `200` OK -> [WarehouseContractListResponseWrapperContract](#model-warehousecontractlistresponsewrappercontract)

---


## WorkOrder

### GET `/v1/work-orders`

Possible includes: ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses InvoiceRelation Country VatInformation VatInformation DeliveryAddresses Country VatInformation Seller Warehouse CostCenter TaskDescription InternalNotes WorkOrderType DeliveryCondition PaymentCondition Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse Hours Employee PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations workorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| offset | query | integer | No |  |
| limit | query | integer | No |  |
| orderBy | query | string | No | FieldName:ASC or FieldName:DESC |
| includeTotalItems | query | boolean | No |  |
| filters | query | string | No |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [WorkOrderContractListResponseWrapperContract](#model-workordercontractlistresponsewrappercontract)

---

### GET `/v1/work-orders/{relationCode}:{entryNumber}`

Possible includes: ServiceObject ConfigurationElements Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Seller SalesRelation Country DeliveryAddresses Groups Product Suppliers Structure Lines Translations WebsiteInformation Relation Country VatInformation VatInformation DeliveryAddresses InvoiceRelation Country VatInformation VatInformation DeliveryAddresses Country VatInformation Seller Warehouse CostCenter TaskDescription InternalNotes WorkOrderType DeliveryCondition PaymentCondition Lines Product Stock Suppliers Relation Country DeliveryAddresses Structure Lines Translations Warehouse Hours Employee PreInvoice Relation Country VatInformation VatInformation DeliveryAddresses SalesOrder Seller Country Lines Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrder ServiceObject ConfigurationElements Product Stock Suppliers Structure Lines Translations Seller Groups Product Suppliers Structure Lines Translations WebsiteInformation Country VatInformation Seller Lines Product Suppliers Structure Lines Translations Hours Delivery Employee Lines Product Suppliers Structure Lines Translations SalesOrderLine ServiceObject ConfigurationElements Groups WebsiteInformation Parcels Items Product Suppliers Structure Lines Translations Invoice PaymentCondition Lines SalesOrderLine Product Suppliers Structure Lines Translations ServiceObject ConfigurationElements Groups WebsiteInformation DeliveryLines WorkOrderLine Product Suppliers Structure Lines Translations Product Suppliers Structure Lines Translations workorders.read

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| include | query | string | No |  |

**Responses:**

- `200` OK -> [WorkOrderContractResponseWrapperContract](#model-workordercontractresponsewrappercontract)

---

### POST `/v1/work-orders/{relationCode}:{entryNumber}/hours`

workorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| body | body | CreateWorkOrderHourContract | No |  |

**Request body:** [CreateWorkOrderHourContract](#model-createworkorderhourcontract)

**Responses:**

- `200` OK

---

### PUT `/v1/work-orders/{relationCode}:{entryNumber}/hours/{id}`

workorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| id | path | string | Yes |  |
| body | body | EditWorkOrderHourContract | No |  |

**Request body:** [EditWorkOrderHourContract](#model-editworkorderhourcontract)

**Responses:**

- `200` OK

---

### DELETE `/v1/work-orders/{relationCode}:{entryNumber}/hours/{id}`

workorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| id | path | string | Yes |  |

**Responses:**

- `200` OK

---

### POST `/v1/work-orders/{relationCode}:{entryNumber}/lines`

workorders.update

**Parameters:**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| relationCode | path | integer | Yes |  |
| entryNumber | path | integer | Yes |  |
| body | body | CreateWorkOrderLineContract | No |  |

**Request body:** [CreateWorkOrderLineContract](#model-createworkorderlinecontract)

**Responses:**

- `200` OK

---



## Data Models

### Model: AcceptOrdersForDebtor

string

### Model: AddFileContract


| Field | Type | Description |
| --- | --- | --- |
| FileId | string (uuid) | Upload the document via the /files endpoint first to get the FileId, or directly fill the FileUrl field |
| FileName | string |  |
| FileUrl | string |  |

### Model: AddFileContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [AddFileContract[]](#addfilecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: AddFileContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [AddFileContract](#addfilecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: AllocateSalesOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| Recnum | integer (int32) |  |
| Quantity | number (double) |  |

### Model: AllocateSalesOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [AllocateSalesOrderLineContract[]](#allocatesalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: AllocateSalesOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [AllocateSalesOrderLineContract](#allocatesalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: AllowedCostCenters

string

### Model: AssemblyType

string

### Model: ConfigurationElementContract


| Field | Type | Description |
| --- | --- | --- |
| SequenceNumber | integer (int32) |  |
| Type | [ConfigurationType](#configurationtype) |  |
| ElementCode | string |  |
| Description | string |  |
| Value | string |  |
| Product | [ProductContract](#productcontract) |  |

### Model: ConfigurationElementContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ConfigurationElementContract[]](#configurationelementcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ConfigurationElementContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ConfigurationElementContract](#configurationelementcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ConfigurationElementIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |

### Model: ConfigurationType

string

### Model: ConnectApiLogContract


| Field | Type | Description |
| --- | --- | --- |
| DateTime | string (date-time) | Format: yyyy-MM-dd |
| Message | string |  |

### Model: ConnectApiLogContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ConnectApiLogContract[]](#connectapilogcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ConnectApiLogContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ConnectApiLogContract](#connectapilogcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContactPersonContract


| Field | Type | Description |
| --- | --- | --- |
| Prefix | string |  |
| LastName | string |  |
| FirstName | string |  |
| Address | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| Fax | string |  |
| EmailAddress1 | string |  |
| EmailAddress2 | string |  |
| Voip | string |  |
| Function | string |  |
| Salutation | string |  |
| Id | string (uuid) |  |
| RelationCode | integer (int32) |  |
| SequenceNumber | integer (int32) |  |
| Active | boolean |  |
| Relation | [RelationContract](#relationcontract) |  |

### Model: ContactPersonContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContactPersonContract[]](#contactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContactPersonContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContactPersonContract](#contactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContractContract


| Field | Type | Description |
| --- | --- | --- |
| ContractNumber | integer (int32) |  |
| RelationCode | integer (int32) |  |
| EntryDate | string (date-time) | Format: yyyy-MM-dd |
| Status | [ContractStatus](#contractstatus) |  |
| Form | [ContractForm](#contractform) |  |
| Type | integer (int32) |  |
| Reference1 | string |  |
| Reference2 | string |  |
| CostCenterCode | integer (int32) |  |
| SellerCode | integer (int32) |  |
| InvoiceRelationCode | integer (int32) |  |
| ContactPersonCode | integer (int32) |  |
| InsurancePercentage | number (double) |  |
| OwnRiskAmount | number (double) |  |
| TransportAmount | number (double) |  |
| UnitType | [ContractUnitType](#contractunittype) |  |
| InvoiceUnitType | [ContractInvoiceUnitType](#contractinvoiceunittype) |  |
| Relation | [RelationContract](#relationcontract) |  |
| InvoiceRelation | [RelationContract](#relationcontract) |  |
| Seller | [EmployeeContract](#employeecontract) |  |
| Lines | [ContractLineContract[]](#contractlinecontract) |  |

### Model: ContractContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContractContract[]](#contractcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContractContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContractContract](#contractcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContractForm

string

### Model: ContractIncludes


| Field | Type | Description |
| --- | --- | --- |
| Relation | [RelationIncludes](#relationincludes) |  |
| InvoiceRelation | [RelationIncludes](#relationincludes) |  |
| Seller | [EmptyIncludes](#emptyincludes) |  |
| Lines | [ContractLineIncludes](#contractlineincludes) |  |

### Model: ContractInvoiceUnitType

string

### Model: ContractLineContract


| Field | Type | Description |
| --- | --- | --- |
| ContractNumber | integer (int32) |  |
| RelationCode | integer (int32) |  |
| ServiceNumber | integer (int32) |  |
| StartDate | string (date-time) | Format: yyyy-MM-dd |
| EndDate | string (date-time) | Format: yyyy-MM-dd |
| Status | [ContractStatus](#contractstatus) |  |
| ActualEndDate | boolean |  |
| PricePerUnit | number (double) |  |
| TransportAmount | number (double) |  |
| OwnRiskAmount | number (double) |  |
| DeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| ReturnDate | string (date-time) | Format: yyyy-MM-dd |
| ExpeditionCode | integer (int32) |  |
| DeliverySequenceNumber | integer (int32) |  |
| FreeText | string |  |
| ServiceObject | [ServiceObjectContract](#serviceobjectcontract) |  |
| Contract | [ContractContract](#contractcontract) |  |

### Model: ContractLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContractLineContract[]](#contractlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContractLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ContractLineContract](#contractlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ContractLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| ServiceObject | [ServiceObjectIncludes](#serviceobjectincludes) |  |
| Contract | [ContractIncludes](#contractincludes) |  |

### Model: ContractStatus

string

### Model: ContractUnitType

string

### Model: CostCenterContract


| Field | Type | Description |
| --- | --- | --- |
| Code | integer (int32) |  |
| Description | string |  |

### Model: CostCenterContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CostCenterContract[]](#costcentercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CostCenterContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CostCenterContract](#costcentercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CostObjectType

string

### Model: CountryContract


| Field | Type | Description |
| --- | --- | --- |
| CountryCode | integer (int32) |  |
| LanguageCode | integer (int32) |  |
| ShortDescription | string |  |
| Description | string |  |
| IsoCode | string |  |
| IsEu | boolean |  |
| VatCode | integer (int32) |  |
| VatInformation | [VatInformationContract](#vatinformationcontract) |  |
| Language | [LanguageContract](#languagecontract) |  |

### Model: CountryContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CountryContract[]](#countrycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CountryContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CountryContract](#countrycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CountryIncludes


| Field | Type | Description |
| --- | --- | --- |
| VatInformation | [EmptyIncludes](#emptyincludes) |  |
| Language | [EmptyIncludes](#emptyincludes) |  |

### Model: CreateContactPersonContract


| Field | Type | Description |
| --- | --- | --- |
| Prefix | string |  |
| LastName | string |  |
| FirstName | string |  |
| Address | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| Fax | string |  |
| EmailAddress1 | string |  |
| EmailAddress2 | string |  |
| Voip | string |  |
| Function | string |  |
| Salutation | string |  |
| RelationId | string (uuid) |  |

### Model: CreateContactPersonContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateContactPersonContract[]](#createcontactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateContactPersonContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateContactPersonContract](#createcontactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateDeliveryAddressContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| ContactPersonCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| DeliveryConditionCode | integer (int32) |  |

### Model: CreateDeliveryAddressContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateDeliveryAddressContract[]](#createdeliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateDeliveryAddressContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateDeliveryAddressContract](#createdeliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateDeliveryContract


| Field | Type | Description |
| --- | --- | --- |
| Reference | string |  |
| RelationCode | integer (int32) |  |
| OrderCosts | number (double) |  |
| ShipmentCosts | number (double) |  |
| ExpeditionCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| EmployeeCode | integer (int32) |  |
| Parcels | [CreateParcelContract[]](#createparcelcontract) |  |

### Model: CreateDeliveryContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateDeliveryContract[]](#createdeliverycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateDeliveryContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateDeliveryContract](#createdeliverycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateJournalEntryContract


| Field | Type | Description |
| --- | --- | --- |
| Reference | string |  |
| BookingText | string |  |
| EntryDate | string (date-time) | Format: yyyy-MM-dd |
| Lines | [CreateJournalEntryLineContract[]](#createjournalentrylinecontract) |  |

### Model: CreateJournalEntryContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateJournalEntryContract[]](#createjournalentrycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateJournalEntryContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateJournalEntryContract](#createjournalentrycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateJournalEntryLineContract


| Field | Type | Description |
| --- | --- | --- |
| GeneralLedgerAccountId | integer (int32) |  |
| CostCenterId | integer (int32) |  |
| DebitAmount | number (double) |  |
| CreditAmount | number (double) |  |
| BookingText | string |  |

### Model: CreateJournalEntryLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateJournalEntryLineContract[]](#createjournalentrylinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateJournalEntryLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateJournalEntryLineContract](#createjournalentrylinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateLastModifiedRuleContract


| Field | Type | Description |
| --- | --- | --- |
| Entity | [LastModifiedRuleType](#lastmodifiedruletype) |  |
| Fields | string[] | The fields to listen on for changes |

### Model: CreateLastModifiedRuleContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateLastModifiedRuleContract[]](#createlastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateLastModifiedRuleContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateLastModifiedRuleContract](#createlastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateParcelContract


| Field | Type | Description |
| --- | --- | --- |
| Description | string |  |
| TrackAndTraceNumber | string |  |
| ExpeditionDate | string (date-time) | Format: yyyy-MM-dd |
| Items | [CreateParcelItemContract[]](#createparcelitemcontract) |  |

### Model: CreateParcelContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateParcelContract[]](#createparcelcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateParcelContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateParcelContract](#createparcelcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateParcelItemContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Quantity | number (double) |  |
| Origin | [ParcelItemOrigin](#parcelitemorigin) |  |
| OriginRecordNumber | integer (int32) |  |

### Model: CreateParcelItemContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateParcelItemContract[]](#createparcelitemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateParcelItemContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateParcelItemContract](#createparcelitemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreatePurchaseInvoiceContract


| Field | Type | Description |
| --- | --- | --- |
| RelationCode | integer (int32) | Relation should be a creditor |
| InvoiceDate | string (date-time) | Format: yyyy-MM-dd |
| PaymentReference | string |  |
| InvoiceAmountIncVat | number (double) |  |
| EntryText | string |  |
| PaymentConditionCode | integer (int32) |  |
| DiscountAmount | number (double) |  |
| CurrencyCode | integer (int32) |  |
| InternalNote | string |  |
| VatCode1 | integer (int32) |  |
| VatAmount1 | number (double) |  |
| VatCode2 | integer (int32) |  |
| VatAmount2 | number (double) |  |
| FiatEmployeeCode | integer (int32) |  |
| Lines | [CreatePurchaseInvoiceLineContract[]](#createpurchaseinvoicelinecontract) |  |
| Documents | [AddFileContract[]](#addfilecontract) | A maximum of five documents are allowed. The first document is considered as the actual invoice |

### Model: CreatePurchaseInvoiceContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreatePurchaseInvoiceContract[]](#createpurchaseinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreatePurchaseInvoiceContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreatePurchaseInvoiceContract](#createpurchaseinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreatePurchaseInvoiceLineContract


| Field | Type | Description |
| --- | --- | --- |
| GeneralLedgerAccountId | integer (int32) |  |
| VatCode | integer (int32) |  |
| Amount | number (double) |  |
| EntryText | string |  |
| CostCenterCode | integer (int32) |  |
| CostObjectNumber | integer (int32) | Can only be filled by general ledger accounts with cost object type 'ServiceObject' and type 'ProfitOrLoss'/'Balance'. The service object must have sales status 'Sold' |

### Model: CreatePurchaseInvoiceLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreatePurchaseInvoiceLineContract[]](#createpurchaseinvoicelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreatePurchaseInvoiceLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreatePurchaseInvoiceLineContract](#createpurchaseinvoicelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateRelationContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| InvoiceEmailAddress | string |  |
| KvkNumber | string |  |
| ContactPerson | string |  |
| VatRegistrationNumber | string |  |
| WebsiteUrl | string |  |
| DebtorDiscountGroup | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| PayVat | boolean |  |
| Type | [RelationType](#relationtype) |  |
| DebtorPaymentConditionCode | integer (int32) |  |
| DebtorDeliveryConditionCode | integer (int32) |  |
| DebtorVatCode | integer (int32) |  |
| GlobalLocationNumber | string |  |
| InternationalBankAccountNumber | string |  |
| InvoiceRelationCode | integer (int32) | Only working when invoice relation entry is enabled in the Powerall sales order/work order/quotation settings |

### Model: CreateRelationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateRelationContract[]](#createrelationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateRelationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateRelationContract](#createrelationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateSalesOrderContract


| Field | Type | Description |
| --- | --- | --- |
| OrderType | integer (int32) |  |
| InvoiceName1 | string |  |
| InvoiceName2 | string |  |
| InvoiceAddressLine | string |  |
| InvoiceZipCode | string |  |
| InvoiceTown | string |  |
| InvoiceCountryCode | integer (int32) |  |
| DeliveryName1 | string |  |
| DeliveryName2 | string |  |
| DeliveryAddressLine | string |  |
| DeliveryZipCode | string |  |
| DeliveryTown | string |  |
| DeliveryCountryCode | integer (int32) |  |
| Reference1 | string |  |
| Reference2 | string |  |
| SellerCode | integer (int32) |  |
| CostCenterCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| PaymentConditionCode | integer (int32) |  |
| ExpeditionCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| RayonCode | string |  |
| SelectionCode | string |  |
| ContactPersonCode | integer (int32) |  |
| AllowPartialDelivery | boolean |  |
| AllowPartialInvoicing | boolean |  |
| TrackAndTraceNumber | string |  |
| Remark | string |  |
| EmailAddress | string |  |
| Phone | string |  |
| ServicePointId | integer (int32) |  |
| ApprovalCode | string |  |
| EntryNumber | integer (int32) | Required when no minimum entry number is set in Powerall. Else, it will be automatically generated |
| RelationId | string | This field can either contain the relation code (numeric), or the relation id (guid) |
| InvoiceRelationId | string | This field can either contain the invoice relation code (numeric), or the invoice relation id (guid) |
| DeliveryAddressId | string | Either fill in this sequence number, or specify the delivery address per field |
| OrderDate | string (date-time) | Format: yyyy-MM-dd |
| DeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| CurrencyCode | integer (int32) |  |
| ApplyWebshopSettings | boolean | When true, specific webshop settings are applied to the order in Powerall |
| ServiceNumber | integer (int32) |  |
| CounterValue1 | integer (int32) |  |
| CounterValue2 | integer (int32) |  |
| InternalNote | string |  |
| Lines | [CreateSalesOrderLineContract[]](#createsalesorderlinecontract) |  |

### Model: CreateSalesOrderContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateSalesOrderContract[]](#createsalesordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateSalesOrderContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateSalesOrderContract](#createsalesordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateSalesOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| LineNumber | integer (int32) | Either leave empty, or provide a contiguous sequence for explicit ordering |
| QuantityOrdered | number (double) |  |
| Description | string |  |
| ExtendedDescription | string |  |
| CustomerReference | string |  |
| DiscountPercentage | number (double) | Fill in with the AppliedDiscountPercentage from /products/prices, or leave empty, so that the API will calculate it for you |
| DeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| InvoiceLineCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| ProductCode | string |  |
| VatCode | integer (int32) |  |
| GrossPrice | number (double) | Fill in with the CustomerGrossPriceExVat from /products/prices, or leave empty, so that the API will calculate it for you |
| PriceIncVat | boolean |  |

### Model: CreateSalesOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateSalesOrderLineContract[]](#createsalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateSalesOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateSalesOrderLineContract](#createsalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateServiceMessageContract


| Field | Type | Description |
| --- | --- | --- |
| MainCategoryId | integer (int32) |  |
| SubCategoryId | integer (int32) |  |
| CreatorEmployeeId | integer (int32) |  |
| DestinationEmployeeId | integer (int32) |  |
| ServiceObjectDescription | string |  |
| ServiceObjectSerialNumber | string |  |
| ServiceObjectRegistrationNumber | string |  |
| ServiceObjectCustomerRegCode | string |  |
| Name | string |  |
| CountryCode | integer (int32) |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| RayonCode | string |  |
| ContactPersonName | string |  |
| ContactPersonEmailAddress | string |  |
| ContactPersonPhone | string |  |
| Subject | string |  |
| OrderData | string |  |
| Priority | [ServiceMessagePriority](#servicemessagepriority) |  |
| RequestDate | string (date-time) | Format: yyyy-MM-dd |
| CreationDate | string (date-time) | Format: yyyy-MM-dd |
| CostCenterCode | integer (int32) |  |
| TravelZoneCode | integer (int32) |  |
| Text | string |  |
| TransferNumber | integer (int32) |  |
| TransferLineNumber | integer (int32) |  |
| ServiceObjectId | string |  |
| RelationId | string |  |
| InternalNotes | [InternalNoteContract[]](#internalnotecontract) |  |
| EstimatedHours | number (double) |  |
| PreferredEmployeeCode | integer (int32) |  |

### Model: CreateServiceMessageContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateServiceMessageContract[]](#createservicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateServiceMessageContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateServiceMessageContract](#createservicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateWorkOrderHourContract


| Field | Type | Description |
| --- | --- | --- |
| WorkDate | string (date-time) | Format: yyyy-MM-dd |
| EmployeeCode | integer (int32) |  |
| TaskTypeId | integer (int32) |  |
| Description | string |  |
| StartTime | string (date-span) |  |
| EndTime | string (date-span) |  |
| BreakTimeMinutes | integer (int32) |  |
| ActualHours | number (double) | Required when no start or end time is specified. |
| InvoiceHours | number (double) |  |
| Percentage | number (double) |  |
| Price | number (double) |  |
| InvoiceLineCode | integer (int32) |  |

### Model: CreateWorkOrderHourContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateWorkOrderHourContract[]](#createworkorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateWorkOrderHourContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateWorkOrderHourContract](#createworkorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateWorkOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Description | string |  |
| QuantityOrdered | number (double) |  |
| QuantityDelivered | number (double) |  |
| DiscountPercentage | number (double) |  |
| VatCode | integer (int32) |  |
| InvoiceLineCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| GrossPrice | number (double) |  |
| PriceIncVat | boolean |  |
| ExtendedDescription | string |  |

### Model: CreateWorkOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateWorkOrderLineContract[]](#createworkorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CreateWorkOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CreateWorkOrderLineContract](#createworkorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CrmAppAccess

string

### Model: CurrencyContract


| Field | Type | Description |
| --- | --- | --- |
| Code | integer (int32) |  |
| Abbreviation | string |  |
| Description | string |  |
| Factor | number (double) |  |

### Model: CurrencyContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CurrencyContract[]](#currencycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: CurrencyContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [CurrencyContract](#currencycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryAddressContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| ContactPersonCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| DeliveryConditionCode | integer (int32) |  |
| Id | string (uuid) |  |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| SequenceNumber | integer (int32) |  |
| Country | [CountryContract](#countrycontract) |  |
| DeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |

### Model: DeliveryAddressContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryAddressContract[]](#deliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryAddressContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryAddressContract](#deliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryAddressIncludes


| Field | Type | Description |
| --- | --- | --- |
| Country | [CountryIncludes](#countryincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |

### Model: DeliveryConditionContract


| Field | Type | Description |
| --- | --- | --- |
| Condition | integer (int32) |  |
| Abbreviation | string |  |
| Description | string |  |

### Model: DeliveryConditionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryConditionContract[]](#deliveryconditioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryConditionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryConditionContract](#deliveryconditioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryContract


| Field | Type | Description |
| --- | --- | --- |
| Reference | string |  |
| RelationCode | integer (int32) |  |
| OrderCosts | number (double) |  |
| ShipmentCosts | number (double) |  |
| ExpeditionCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| EmployeeCode | integer (int32) |  |
| DeliveryNumber | integer (int32) |  |
| WarehouseTo | integer (int32) |  |
| Status | [DeliveryStatus](#deliverystatus) |  |
| PreInvoiceRelationCode | integer (int32) |  |
| PreInvoiceEntryNumber | integer (int32) |  |
| PreInvoice | [PreInvoiceContract](#preinvoicecontract) |  |
| EmployeeContract | [EmployeeContract](#employeecontract) |  |
| Lines | [DeliveryLineContract[]](#deliverylinecontract) |  |
| Parcels | [ParcelContract[]](#parcelcontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| DeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |

### Model: DeliveryContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryContract[]](#deliverycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryContract](#deliverycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryIncludes


| Field | Type | Description |
| --- | --- | --- |
| PreInvoice | [PreInvoiceIncludes](#preinvoiceincludes) |  |
| Employee | [EmptyIncludes](#emptyincludes) |  |
| Lines | [DeliveryLineIncludes](#deliverylineincludes) |  |
| Parcels | [ParcelIncludes](#parcelincludes) |  |
| Relation | [RelationIncludes](#relationincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |

### Model: DeliveryLineContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| DeliveryNumber | integer (int32) |  |
| SequenceNumber | integer (int32) |  |
| SalesOrderLineRecordNumber | integer (int32) |  |
| ProductCode | string |  |
| Quantity | number (double) |  |
| TrackAndTraceNumber | string |  |
| Product | [ProductContract](#productcontract) |  |
| SalesOrderLine | [SalesOrderLineContract](#salesorderlinecontract) |  |

### Model: DeliveryLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryLineContract[]](#deliverylinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DeliveryLineContract](#deliverylinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DeliveryLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |
| SalesOrderLine | [SalesOrderLineIncludes](#salesorderlineincludes) |  |

### Model: DeliveryStatus

string

### Model: DossierItemContract


| Field | Type | Description |
| --- | --- | --- |
| Index | integer (int32) |  |
| LastModified | string (date-time) | Format: yyyy-MM-dd |
| FileName | string |  |
| FileType | [DossierItemType](#dossieritemtype) |  |
| Url | string |  |

### Model: DossierItemContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DossierItemContract[]](#dossieritemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DossierItemContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [DossierItemContract](#dossieritemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: DossierItemType

string

### Model: EDocumentEmailAddressContract


| Field | Type | Description |
| --- | --- | --- |
| Type | [EDocumentEmailAddressType](#edocumentemailaddresstype) |  |
| EmailAddress | string |  |

### Model: EDocumentEmailAddressType

string

### Model: EditContactPersonContract


| Field | Type | Description |
| --- | --- | --- |
| Prefix | string |  |
| LastName | string |  |
| FirstName | string |  |
| Address | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| Fax | string |  |
| EmailAddress1 | string |  |
| EmailAddress2 | string |  |
| Voip | string |  |
| Function | string |  |
| Salutation | string |  |

### Model: EditContactPersonContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditContactPersonContract[]](#editcontactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditContactPersonContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditContactPersonContract](#editcontactpersoncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditDeliveryAddressContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| ContactPersonCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| DeliveryConditionCode | integer (int32) |  |

### Model: EditDeliveryAddressContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditDeliveryAddressContract[]](#editdeliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditDeliveryAddressContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditDeliveryAddressContract](#editdeliveryaddresscontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditLastModifiedRuleContract


| Field | Type | Description |
| --- | --- | --- |
| Fields | string[] | The fields to listen on for changes |

### Model: EditLastModifiedRuleContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditLastModifiedRuleContract[]](#editlastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditLastModifiedRuleContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditLastModifiedRuleContract](#editlastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditRelationContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| InvoiceEmailAddress | string |  |
| KvkNumber | string |  |
| ContactPerson | string |  |
| VatRegistrationNumber | string |  |
| WebsiteUrl | string |  |
| DebtorDiscountGroup | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| PayVat | boolean |  |
| Type | [RelationType](#relationtype) |  |
| DebtorPaymentConditionCode | integer (int32) |  |
| DebtorDeliveryConditionCode | integer (int32) |  |
| DebtorVatCode | integer (int32) |  |
| GlobalLocationNumber | string |  |
| InternationalBankAccountNumber | string |  |

### Model: EditRelationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditRelationContract[]](#editrelationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditRelationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditRelationContract](#editrelationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditServiceMessageContract


| Field | Type | Description |
| --- | --- | --- |
| MainCategoryId | integer (int32) |  |
| SubCategoryId | integer (int32) |  |
| CreatorEmployeeId | integer (int32) |  |
| DestinationEmployeeId | integer (int32) |  |
| ServiceObjectDescription | string |  |
| ServiceObjectSerialNumber | string |  |
| ServiceObjectRegistrationNumber | string |  |
| ServiceObjectCustomerRegCode | string |  |
| Name | string |  |
| CountryCode | integer (int32) |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| RayonCode | string |  |
| ContactPersonName | string |  |
| ContactPersonEmailAddress | string |  |
| ContactPersonPhone | string |  |
| Subject | string |  |
| OrderData | string |  |
| Priority | [ServiceMessagePriority](#servicemessagepriority) |  |
| RequestDate | string (date-time) | Format: yyyy-MM-dd |
| CreationDate | string (date-time) | Format: yyyy-MM-dd |
| CostCenterCode | integer (int32) |  |
| TravelZoneCode | integer (int32) |  |
| Text | string |  |
| TransferNumber | integer (int32) |  |
| TransferLineNumber | integer (int32) |  |
| ServiceObjectId | string |  |
| RelationId | string |  |

### Model: EditServiceMessageContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditServiceMessageContract[]](#editservicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditServiceMessageContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditServiceMessageContract](#editservicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditWorkOrderHourContract


| Field | Type | Description |
| --- | --- | --- |
| WorkDate | string (date-time) | Format: yyyy-MM-dd |
| EmployeeCode | integer (int32) |  |
| TaskTypeId | integer (int32) |  |
| Description | string |  |
| StartTime | string (date-span) |  |
| EndTime | string (date-span) |  |
| BreakTimeMinutes | integer (int32) |  |
| ActualHours | number (double) | Required when no start or end time is specified. |
| InvoiceHours | number (double) |  |
| Percentage | number (double) |  |
| Price | number (double) |  |
| InvoiceLineCode | integer (int32) |  |

### Model: EditWorkOrderHourContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditWorkOrderHourContract[]](#editworkorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EditWorkOrderHourContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EditWorkOrderHourContract](#editworkorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EmployeeContract


| Field | Type | Description |
| --- | --- | --- |
| EmployeeCode | integer (int32) |  |
| ShortName | string |  |
| Name | string |  |
| RelationCode | integer (int32) |  |
| DateEmployed | string (date-time) | Format: yyyy-MM-dd |
| DateUnEmployed | string (date-time) | Format: yyyy-MM-dd |
| DateOfBirth | string (date-time) | Format: yyyy-MM-dd |
| Phone | string |  |
| UseCrmApp | boolean |  |
| CrmAppRelationAccess | [CrmAppAccess](#crmappaccess) |  |
| CrmAppContactAccess | [CrmAppAccess](#crmappaccess) |  |
| CrmAppMachineAccess | [CrmAppAccess](#crmappaccess) |  |
| CrmAppShowPurchasePrice | boolean |  |
| CrmAppShowQuotation | boolean |  |
| Function | string |  |

### Model: EmployeeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EmployeeContract[]](#employeecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EmployeeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [EmployeeContract](#employeecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: EmptyIncludes

object

### Model: ExpectedGoodsReceiptBookingContract


| Field | Type | Description |
| --- | --- | --- |
| Lines | [ExpectedGoodsReceiptBookingLineContract[]](#expectedgoodsreceiptbookinglinecontract) |  |

### Model: ExpectedGoodsReceiptBookingContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptBookingContract[]](#expectedgoodsreceiptbookingcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptBookingContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptBookingContract](#expectedgoodsreceiptbookingcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptBookingLineContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| Quantity | number (double) |  |

### Model: ExpectedGoodsReceiptBookingLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptBookingLineContract[]](#expectedgoodsreceiptbookinglinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptBookingLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptBookingLineContract](#expectedgoodsreceiptbookinglinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptContract


| Field | Type | Description |
| --- | --- | --- |
| EntryNumber | integer (int32) |  |
| SupplierRelationCode | integer (int32) |  |
| EntryDate | string (date-time) | Format: yyyy-MM-dd |
| ExpectedDate | string (date-time) | Format: yyyy-MM-dd |
| Reference | string |  |
| SupplierReference | string |  |
| WarehouseCode | integer (int32) |  |
| Status | [ExpectedGoodsReceiptStatus](#expectedgoodsreceiptstatus) |  |
| Lines | [ExpectedGoodsReceiptLineContract[]](#expectedgoodsreceiptlinecontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |
| Supplier | [RelationContract](#relationcontract) |  |

### Model: ExpectedGoodsReceiptContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptContract[]](#expectedgoodsreceiptcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptContract](#expectedgoodsreceiptcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptLineContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| ProductCode | string |  |
| PurchaseProductCode | string |  |
| Quantity | number (double) |  |
| PurchaseQuantity | integer (int32) |  |
| PurchaseUnit | string |  |
| GrossPurchasePrice | number (double) |  |
| NetPurchasePrice | number (double) |  |
| PurchasePriceQuantity | integer (int32) |  |
| PurchasePriceUnit | string |  |
| Origin | [ExpectedGoodsReceiptLineOrigin](#expectedgoodsreceiptlineorigin) |  |
| OriginRecordNumber | integer (int32) |  |
| Product | [ProductContract](#productcontract) |  |
| PurchaseOrderLine | [PurchaseOrderLineContract](#purchaseorderlinecontract) |  |

### Model: ExpectedGoodsReceiptLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptLineContract[]](#expectedgoodsreceiptlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ExpectedGoodsReceiptLineContract](#expectedgoodsreceiptlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ExpectedGoodsReceiptLineOrigin

string

### Model: ExpectedGoodsReceiptStatus

string

### Model: FileIdContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |

### Model: FileIdContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [FileIdContract[]](#fileidcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: FileIdContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [FileIdContract](#fileidcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: GeneralLedgerAccountContract


| Field | Type | Description |
| --- | --- | --- |
| Id | integer (int32) |  |
| Description | string |  |
| IsActive | boolean |  |
| Type | [GeneralLedgerAccountType](#generalledgeraccounttype) |  |
| AllowedCostCenters | [AllowedCostCenters](#allowedcostcenters) |  |
| CostCenterId | integer (int32) |  |
| CostObjectType | [CostObjectType](#costobjecttype) |  |
| IsSubAdministration | boolean |  |
| LastModified | string (date-time) | Format: yyyy-MM-dd |

### Model: GeneralLedgerAccountContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [GeneralLedgerAccountContract[]](#generalledgeraccountcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: GeneralLedgerAccountContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [GeneralLedgerAccountContract](#generalledgeraccountcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: GeneralLedgerAccountType

string

### Model: IdContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |

### Model: IdContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [IdContract[]](#idcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: IdContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [IdContract](#idcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: InternalNoteContract


| Field | Type | Description |
| --- | --- | --- |
| CreationDate | string (date-time) | Format: yyyy-MM-dd |
| CreationTime | string (date-span) |  |
| Text | string |  |
| CreatorEmployeeId | integer (int32) |  |

### Model: InternalNoteContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [InternalNoteContract[]](#internalnotecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: InternalNoteContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [InternalNoteContract](#internalnotecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: InvoiceContract


| Field | Type | Description |
| --- | --- | --- |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| InvoiceNumber | integer (int32) |  |
| InvoiceDate | string (date-time) | Format: yyyy-MM-dd |
| Reference | string |  |
| InvoiceAmount | number (double) |  |
| TotalPaid | number (double) |  |
| IsPaid | boolean |  |
| NumberOfPreInvoices | integer (int32) |  |
| PaymentCondition | [PaymentConditionContract](#paymentconditioncontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| PdfUrl | string |  |
| PreInvoices | [PreInvoiceContract[]](#preinvoicecontract) |  |

### Model: InvoiceContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [InvoiceContract[]](#invoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: InvoiceContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [InvoiceContract](#invoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: InvoiceIncludes


| Field | Type | Description |
| --- | --- | --- |
| Relation | [RelationIncludes](#relationincludes) |  |
| PreInvoices | [PreInvoiceIncludes](#preinvoiceincludes) |  |

### Model: JournalContract


| Field | Type | Description |
| --- | --- | --- |
| GeneralLedgerJournalId | integer (int32) |  |
| Description | string |  |
| TypeOfJournal | string |  |
| GeneralLedgerAccountId | integer (int32) |  |

### Model: JournalContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [JournalContract[]](#journalcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: JournalContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [JournalContract](#journalcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: KeyValueContract


| Field | Type | Description |
| --- | --- | --- |
| Field | string |  |
| Value |  |  |

### Model: KeyValueContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [KeyValueContract[]](#keyvaluecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: KeyValueContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [KeyValueContract](#keyvaluecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: LanguageContract


| Field | Type | Description |
| --- | --- | --- |
| LanguageCode | integer (int32) |  |
| Description | string |  |
| IsoLanguageCode | string |  |

### Model: LastModifiedRuleContract


| Field | Type | Description |
| --- | --- | --- |
| Entity | [LastModifiedRuleType](#lastmodifiedruletype) |  |
| Fields | string[] |  |

### Model: LastModifiedRuleContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [LastModifiedRuleContract[]](#lastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: LastModifiedRuleContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [LastModifiedRuleContract](#lastmodifiedrulecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: LastModifiedRuleType

string

### Model: ParcelContract


| Field | Type | Description |
| --- | --- | --- |
| Description | string |  |
| TrackAndTraceNumber | string |  |
| ExpeditionDate | string (date-time) | Format: yyyy-MM-dd |
| ParcelNumber | integer (int32) |  |
| DeliveryNumber | integer (int32) |  |
| Items | [ParcelItemContract[]](#parcelitemcontract) |  |
| Delivery | [DeliveryContract](#deliverycontract) |  |

### Model: ParcelContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ParcelContract[]](#parcelcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ParcelContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ParcelContract](#parcelcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ParcelIncludes


| Field | Type | Description |
| --- | --- | --- |
| Items | [ParcelItemIncludes](#parcelitemincludes) |  |
| Delivery | [DeliveryIncludes](#deliveryincludes) |  |

### Model: ParcelItemContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Quantity | number (double) |  |
| ParcelNumber | integer (int32) |  |
| Description | string |  |
| Product | [ProductContract](#productcontract) |  |

### Model: ParcelItemContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ParcelItemContract[]](#parcelitemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ParcelItemContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ParcelItemContract](#parcelitemcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ParcelItemIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |

### Model: ParcelItemOrigin

string

### Model: PaymentConditionContract


| Field | Type | Description |
| --- | --- | --- |
| Condition | integer (int32) |  |
| Abbreviation | string |  |
| Description | string |  |
| PaymentTerm | integer (int32) |  |

### Model: PaymentConditionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PaymentConditionContract[]](#paymentconditioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PaymentConditionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PaymentConditionContract](#paymentconditioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: Permission

string

### Model: PermissionContract


| Field | Type | Description |
| --- | --- | --- |
| Scope | [Scope](#scope) |  |
| Permission | [Permission](#permission) |  |

### Model: PermissionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PermissionContract[]](#permissioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PermissionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PermissionContract](#permissioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PickSalesOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| Recnum | integer (int32) |  |
| Quantity | number (double) |  |

### Model: PickSalesOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PickSalesOrderLineContract[]](#picksalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PickSalesOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PickSalesOrderLineContract](#picksalesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PicklistContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| Type | [PicklistType](#picklisttype) |  |
| Key | integer (int64) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| Status | integer (int32) |  |
| First | boolean |  |
| ShipmentId | integer (int32) |  |
| TaskNumber | integer (int32) |  |
| Description | string |  |
| Lines | [PicklistLineContract[]](#picklistlinecontract) |  |

### Model: PicklistContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PicklistContract[]](#picklistcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PicklistContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PicklistContract](#picklistcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PicklistLineContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| Key | integer (int64) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| OriginRecordNumber | integer (int32) |  |
| Status | integer (int32) |  |
| Quantity | number (double) |  |
| Location | string |  |
| ProductCode | string |  |
| ParcelItem | [ParcelItemContract](#parcelitemcontract) |  |

### Model: PicklistLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PicklistLineContract[]](#picklistlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PicklistLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PicklistLineContract](#picklistlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PicklistType

string

### Model: PreInvoiceContract


| Field | Type | Description |
| --- | --- | --- |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| EntryDate | string (date-time) | Format: yyyy-MM-dd |
| InvoiceNumber | integer (int32) |  |
| InvoiceDate | string (date-time) | Format: yyyy-MM-dd |
| Reference1 | string |  |
| Reference2 | string |  |
| Status | [PreInvoiceStatus](#preinvoicestatus) |  |
| NumDeliveries | integer (int32) |  |
| InvoiceName1 | string |  |
| InvoiceName2 | string |  |
| InvoiceAddressLine | string |  |
| InvoiceZipCode | string |  |
| InvoiceTown | string |  |
| InvoiceCountryCode | integer (int32) |  |
| DeliveryName1 | string |  |
| DeliveryName2 | string |  |
| DeliveryAddressLine | string |  |
| DeliveryZipCode | string |  |
| DeliveryTown | string |  |
| DeliveryCountryCode | integer (int32) |  |
| DeliverySequenceNumber | integer (int32) |  |
| DiscountPercentage | number (double) |  |
| PaymentConditionCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| ServiceNumber | integer (int32) |  |
| InvoiceAmountInc | number (double) |  |
| InvoiceAmountEx | number (double) |  |
| CollectiveInvoice | boolean |  |
| ExpectedDeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| HoursQuantity | number (double) |  |
| Origin | [PreInvoiceOrigin](#preinvoiceorigin) |  |
| OriginEntryNumber | integer (int32) |  |
| OriginRelationCode | integer (int32) |  |
| ExpeditionCode | integer (int32) |  |
| HoursAmount | number (double) |  |
| SellerCode | integer (int32) |  |
| SelectionCode | string |  |
| Relation | [RelationContract](#relationcontract) |  |
| Invoice | [InvoiceContract](#invoicecontract) |  |
| Delivery | [DeliveryContract](#deliverycontract) |  |
| SalesOrder | [SalesOrderContract](#salesordercontract) |  |
| WorkOrder | [WorkOrderContract](#workordercontract) |  |
| PaymentCondition | [PaymentConditionContract](#paymentconditioncontract) |  |
| DeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |
| Seller | [EmployeeContract](#employeecontract) |  |
| Lines | [PreInvoiceLineContract[]](#preinvoicelinecontract) |  |

### Model: PreInvoiceContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PreInvoiceContract[]](#preinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PreInvoiceContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PreInvoiceContract](#preinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PreInvoiceIncludes


| Field | Type | Description |
| --- | --- | --- |
| Relation | [RelationIncludes](#relationincludes) |  |
| SalesOrder | [SalesOrderIncludes](#salesorderincludes) |  |
| WorkOrder | [WorkOrderIncludes](#workorderincludes) |  |
| Delivery | [DeliveryIncludes](#deliveryincludes) |  |
| Invoice | [InvoiceIncludes](#invoiceincludes) |  |
| PaymentCondition | [EmptyIncludes](#emptyincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |
| Lines | [PreInvoiceLineIncludes](#preinvoicelineincludes) |  |
| Seller | [EmptyIncludes](#emptyincludes) |  |

### Model: PreInvoiceLineContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| LineNumber | integer (int32) |  |
| LineType | [PreInvoiceLineType](#preinvoicelinetype) |  |
| ProductCode | string |  |
| Description1 | string |  |
| Description2 | string |  |
| FinalSalesPrice | number (double) |  |
| OrderedQuantity | number (double) |  |
| DeliveredQuantity | number (double) |  |
| DiscountPercentage | number (double) |  |
| ExpectedDeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| InvoiceLineCode | integer (int32) |  |
| InvoiceLineText | string |  |
| FinancialGroup | integer (int32) |  |
| SuppressionType | [SuppressionType](#suppressiontype) |  |
| VatCode | integer (int32) |  |
| SalesPriceUnit | string |  |
| SalesPriceQuantity | integer (int32) |  |
| SalesUnit | string |  |
| SalesQuantity | integer (int32) |  |
| CustomerReference | string |  |
| ServiceNumber | integer (int32) |  |
| IsIncVatPrice | boolean |  |
| Origin | string |  |
| OriginRecordNumber | integer (int32) |  |
| AssemblyType | [AssemblyType](#assemblytype) |  |
| Product | [ProductContract](#productcontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |
| SalesOrderLine | [SalesOrderLineContract](#salesorderlinecontract) |  |
| WorkOrderLine | [WorkOrderLineContract](#workorderlinecontract) |  |

### Model: PreInvoiceLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PreInvoiceLineContract[]](#preinvoicelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PreInvoiceLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PreInvoiceLineContract](#preinvoicelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PreInvoiceLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| SalesOrderLine | [SalesOrderLineIncludes](#salesorderlineincludes) |  |
| WorkOrderLine | [WorkOrderLineIncludes](#workorderlineincludes) |  |
| Warehouse | [EmptyIncludes](#emptyincludes) |  |
| Product | [ProductIncludes](#productincludes) |  |

### Model: PreInvoiceLineType

string

### Model: PreInvoiceOrigin

string

### Model: PreInvoiceStatus

string

### Model: PriceAgreementContract


| Field | Type | Description |
| --- | --- | --- |
| RelationCode | integer (int32) |  |
| DiscountGroup | string |  |
| ProductCode | string |  |
| FinancialGroup | integer (int32) |  |
| Quantity | number (double) |  |
| SalesPrice | number (double) |  |
| DiscountOnOrderType1 | number (double) |  |
| DiscountOnOrderType2 | number (double) |  |
| DiscountOnOrderType3 | number (double) |  |
| DiscountOnOrderType4 | number (double) |  |
| DiscountOnOrderType5 | number (double) |  |
| CostPriceFactor | number (double) |  |

### Model: PriceAgreementContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceAgreementContract[]](#priceagreementcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PriceAgreementContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceAgreementContract](#priceagreementcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PriceRequestContract


| Field | Type | Description |
| --- | --- | --- |
| CountryCode | string |  |
| RelationCode | integer (int32) |  |
| OrderType | integer (int32) |  |
| Lines | [PriceRequestLineContract[]](#pricerequestlinecontract) |  |

### Model: PriceRequestContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceRequestContract[]](#pricerequestcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PriceRequestContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceRequestContract](#pricerequestcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PriceRequestLineContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Quantity | number (double) |  |

### Model: PriceRequestLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceRequestLineContract[]](#pricerequestlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PriceRequestLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PriceRequestLineContract](#pricerequestlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProcessStatus

string

### Model: ProductContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Description1 | string |  |
| Description2 | string |  |
| FinancialGroup | integer (int32) |  |
| FinancialGroupDescription | string |  |
| MainGroup | string |  |
| MainGroupDescription | string |  |
| SubGroup | string |  |
| SubGroupDescription | string |  |
| SubSubGroup | string |  |
| SubSubGroupDescription | string |  |
| SelectionCode1 | string |  |
| SelectionCode1Description | string |  |
| SelectionCode2 | string |  |
| SelectionCode2Description | string |  |
| SelectionCode3 | string |  |
| SelectionCode3Description | string |  |
| SelectionCode4 | string |  |
| SelectionCode4Description | string |  |
| SalesPriceUnit | string |  |
| SalesPriceQuantity | integer (int32) |  |
| SalesUnit | string |  |
| SalesQuantity | integer (int32) |  |
| DateCreated | string (date-time) | Format: yyyy-MM-dd |
| SearchName | string |  |
| EanCode | string |  |
| Type | [ProductType](#producttype) |  |
| Weight | number (double) |  |
| EquivalentCode | string |  |
| NewProductCode | string |  |
| MakeCode | string |  |
| HideOnWebshop | boolean |  |
| SearchText | string |  |
| Color | string |  |
| Size | string |  |
| ReplacesProductCodes | string[] |  |
| Status | [ProductStatus](#productstatus) |  |
| IsStockKeeping | boolean |  |
| LastModified | string (date-time) | Format: yyyy-MM-dd |
| TracingType | [ProductTracingType](#producttracingtype) |  |
| SalesPrice | number (double) |  |
| SalesPriceIsIncVat | boolean |  |
| AdvicePrice | number (double) |  |
| PromotionalPrice | number (double) |  |
| TransferPrice | number (double) |  |
| StockPerWarehouse | [ProductStockContract[]](#productstockcontract) |  |
| Make | [ProductMakeContract](#productmakecontract) |  |
| VatInformation | [VatInformationContract](#vatinformationcontract) |  |
| Translations | [ProductTranslationContract[]](#producttranslationcontract) |  |
| Suppliers | [ProductSupplierContract[]](#productsuppliercontract) |  |
| Properties | [ProductPropertyContract[]](#productpropertycontract) |  |
| DossierItems | [DossierItemContract[]](#dossieritemcontract) |  |
| Structure | [ProductStructureContract](#productstructurecontract) |  |

### Model: ProductContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductContract[]](#productcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductContract](#productcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductGroupContractFlat


| Field | Type | Description |
| --- | --- | --- |
| MainGroupCode | string |  |
| SubGroupCode | string |  |
| SubSubGroupCode | string |  |
| Description | string |  |

### Model: ProductGroupContractFlatListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductGroupContractFlat[]](#productgroupcontractflat) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductGroupContractFlatResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductGroupContractFlat](#productgroupcontractflat) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductIncludes


| Field | Type | Description |
| --- | --- | --- |
| Stock | [EmptyIncludes](#emptyincludes) |  |
| Make | [EmptyIncludes](#emptyincludes) |  |
| Suppliers | [SupplierIncludes](#supplierincludes) |  |
| DossierItems | [EmptyIncludes](#emptyincludes) |  |
| Properties | [EmptyIncludes](#emptyincludes) |  |
| GroupDescriptions | [EmptyIncludes](#emptyincludes) |  |
| Structure | [ProductStructureIncludes](#productstructureincludes) |  |
| FinancialGroupDescription | [EmptyIncludes](#emptyincludes) |  |
| SelectionCodeDescriptions | [EmptyIncludes](#emptyincludes) |  |
| Translations | [StringEmptyIncludesListIncludes](#stringemptyincludeslistincludes) |  |

### Model: ProductMakeContract


| Field | Type | Description |
| --- | --- | --- |
| Code | string |  |
| Description | string |  |

### Model: ProductMakeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMakeContract[]](#productmakecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMakeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMakeContract](#productmakecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMutationContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| Date | string (date-time) | Format: yyyy-MM-dd |
| Type | [ProductMutationType](#productmutationtype) |  |
| Quantity | number (double) |  |
| ProductCode | string |  |
| WarehouseCode | integer (int32) |  |
| DestinationWarehouseCode | integer (int32) |  |
| PurchaseEntryNumber | integer (int32) |  |
| FinancialGroup | integer (int32) |  |
| CostPrice | number (double) |  |
| SalesPrice | number (double) |  |
| OriginalPrice | number (double) |  |
| SalesUnit | string |  |
| SalesQuantity | integer (int32) |  |
| SalesPriceUnit | string |  |
| SalesPriceQuantity | integer (int32) |  |
| QuantityMatched | number (double) |  |
| FullyMatched | boolean |  |
| CounterAccountId | integer (int32) |  |
| ServiceNumber | integer (int32) |  |
| Product | [ProductContract](#productcontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |
| DestinationWarehouse | [WarehouseContract](#warehousecontract) |  |
| ServiceObject | [ServiceObjectContract](#serviceobjectcontract) |  |

### Model: ProductMutationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMutationContract[]](#productmutationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMutationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMutationContract](#productmutationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMutationMatchContract


| Field | Type | Description |
| --- | --- | --- |
| RecordNumber | integer (int32) |  |
| Quantity | number (double) |  |

### Model: ProductMutationMatchContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMutationMatchContract[]](#productmutationmatchcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMutationMatchContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductMutationMatchContract](#productmutationmatchcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductMutationType

string

### Model: ProductPriceContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Quantity | number (double) |  |
| GrossPriceExVat | number (double) |  |
| GrossPriceIncVat | number (double) |  |
| CustomerGrossPriceExVat | number (double) |  |
| CustomerGrossPriceIncVat | number (double) |  |
| NetPriceExVat | number (double) |  |
| NetPriceIncVat | number (double) |  |
| AppliedDiscountPercentage | number (double) |  |
| AppliedAgreement | [PriceAgreementContract](#priceagreementcontract) |  |
| QuantityDiscounts | [QuantityDiscountContract[]](#quantitydiscountcontract) |  |

### Model: ProductPriceContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductPriceContract[]](#productpricecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductPriceContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductPriceContract](#productpricecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductPropertyContract


| Field | Type | Description |
| --- | --- | --- |
| Code | string |  |
| Description | string |  |
| IsNumeric | boolean |  |
| Value | string |  |

### Model: ProductPropertyContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductPropertyContract[]](#productpropertycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductPropertyContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductPropertyContract](#productpropertycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStatus

string

### Model: ProductStockContract


| Field | Type | Description |
| --- | --- | --- |
| Location1 | string |  |
| Location2 | string |  |
| ShelfStock | number (double) |  |
| FreeStock | number (double) |  |
| EconomicalStock | number (double) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |

### Model: ProductStockContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockContract[]](#productstockcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStockContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockContract](#productstockcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStockCorrectionContract


| Field | Type | Description |
| --- | --- | --- |
| MutationDate | string (date-time) | Format: yyyy-MM-dd |
| WarehouseCode | integer (int32) |  |
| Reference | string |  |
| Lines | [ProductStockCorrectionLineContract[]](#productstockcorrectionlinecontract) |  |

### Model: ProductStockCorrectionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockCorrectionContract[]](#productstockcorrectioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStockCorrectionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockCorrectionContract](#productstockcorrectioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStockCorrectionLineContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Quantity | number (double) |  |

### Model: ProductStockCorrectionLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockCorrectionLineContract[]](#productstockcorrectionlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStockCorrectionLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStockCorrectionLineContract](#productstockcorrectionlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStructureContract


| Field | Type | Description |
| --- | --- | --- |
| Type | [ProductStructureType](#productstructuretype) |  |
| Description | string |  |
| Lines | [ProductStructureLineContract[]](#productstructurelinecontract) |  |

### Model: ProductStructureContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStructureContract[]](#productstructurecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStructureContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStructureContract](#productstructurecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStructureIncludes


| Field | Type | Description |
| --- | --- | --- |
| Lines | [ProductStructureLineIncludes](#productstructurelineincludes) |  |

### Model: ProductStructureLineContract


| Field | Type | Description |
| --- | --- | --- |
| LineNumber | integer (int32) |  |
| ProductCode | string |  |
| Description | string |  |
| Quantity | number (double) |  |
| InvoiceLineCode | integer (int32) |  |
| Product | [ProductContract](#productcontract) |  |

### Model: ProductStructureLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStructureLineContract[]](#productstructurelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStructureLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductStructureLineContract](#productstructurelinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductStructureLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |

### Model: ProductStructureType

string

### Model: ProductSupplierContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| RelationCode | integer (int32) |  |
| PurchaseProductCode | string |  |
| PurchaseDeliveryTime | integer (int32) |  |
| AverageDeliveryTime | integer (int32) |  |
| IsPreferredSupplier | boolean |  |
| IsPricePreferredSupplier | boolean |  |
| PurchaseQuantityByUnit | number (double) |  |
| Relation | [RelationContract](#relationcontract) |  |

### Model: ProductTracingType

string

### Model: ProductTranslationContract


| Field | Type | Description |
| --- | --- | --- |
| IsoLanguageCode | string |  |
| Description1 | string |  |
| Description2 | string |  |
| Text | string |  |
| SearchText | string |  |

### Model: ProductTranslationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductTranslationContract[]](#producttranslationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductTranslationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ProductTranslationContract](#producttranslationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ProductType

string

### Model: PurchaseInvoiceApproveContract


| Field | Type | Description |
| --- | --- | --- |
| EmployeeCode | integer (int32) |  |
| Date | string (date-time) | Format: yyyy-MM-dd |
| Time | string (time) |  |
| NextEmployeeCode | integer (int32) | When Final is false, the employee that has to give the next approval. Otherwise, this field must be empty |
| Final | boolean | When false, the status of the invoice does not change. When true, the invoice becomes payable. |

### Model: PurchaseInvoiceApproveContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceApproveContract[]](#purchaseinvoiceapprovecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseInvoiceApproveContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceApproveContract](#purchaseinvoiceapprovecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseInvoiceContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |
| RelationCode | integer (int32) |  |
| InvoiceNumber | integer (int32) |  |
| InvoiceDate | string (date-time) | Format: yyyy-MM-dd |
| PaymentReference | string |  |
| InvoiceAmountIncVat | number (double) |  |
| EntryText | string |  |
| DiscountAmount | number (double) |  |
| PaymentConditionCode | integer (int32) |  |
| CurrencyCode | integer (int32) |  |
| InternalNote | string |  |

### Model: PurchaseInvoiceContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceContract[]](#purchaseinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseInvoiceContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceContract](#purchaseinvoicecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseInvoiceFiatContract


| Field | Type | Description |
| --- | --- | --- |
| EmployeeCode | integer (int32) |  |
| Date | string (date-time) | Format: yyyy-MM-dd |
| Time | string (time) |  |
| NextEmployeeCode | integer (int32) | When Final is true, the employee that has to approve the invoice now. When Final is false, the employee that has to give the next fiat. |
| Final | boolean | When false, the status of the invoice does not change. When true, the invoice moves to the approval stage. |

### Model: PurchaseInvoiceFiatContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceFiatContract[]](#purchaseinvoicefiatcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseInvoiceFiatContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseInvoiceFiatContract](#purchaseinvoicefiatcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseOrderContract


| Field | Type | Description |
| --- | --- | --- |
| Status | [PurchaseOrderStatus](#purchaseorderstatus) |  |
| SelectionCode | string |  |
| OrderDate | string (date-time) | Format: yyyy-MM-dd |
| Reference1 | string |  |
| Reference2 | string |  |
| EmployeeCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| SupplierEntryNumber | string |  |
| InvoiceName1 | string |  |
| InvoiceName2 | string |  |
| InvoiceAddressLine | string |  |
| InvoiceZipCode | string |  |
| InvoiceTown | string |  |
| InvoiceCountryCode | integer (int32) |  |
| DeliveryName1 | string |  |
| DeliveryName2 | string |  |
| DeliveryAddressLine | string |  |
| DeliveryZipCode | string |  |
| DeliveryTown | string |  |
| DeliveryCountryCode | integer (int32) |  |
| OrderType | integer (int32) |  |
| Id | string (uuid) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| InvoiceCountry | [CountryContract](#countrycontract) |  |
| DeliveryCountry | [CountryContract](#countrycontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |
| Lines | [PurchaseOrderLineContract[]](#purchaseorderlinecontract) |  |

### Model: PurchaseOrderContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseOrderContract[]](#purchaseordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseOrderContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseOrderContract](#purchaseordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseOrderIncludes


| Field | Type | Description |
| --- | --- | --- |
| Lines | [PurchaseOrderLineIncludes](#purchaseorderlineincludes) |  |
| Relation | [RelationIncludes](#relationincludes) |  |
| Warehouse | [EmptyIncludes](#emptyincludes) |  |
| InvoiceCountry | [CountryIncludes](#countryincludes) |  |
| DeliveryCountry | [CountryIncludes](#countryincludes) |  |

### Model: PurchaseOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |
| LineNumber | integer (int32) |  |
| RecordNumber | integer (int32) |  |
| ProductCode | string |  |
| PurchaseNumber | string |  |
| PurchaseGrossPrice | number (double) |  |
| DiscountPercentage | number (double) |  |
| VatCode | integer (int32) |  |
| PurchaseUnit | string |  |
| PurchaseQuantity | integer (int32) |  |
| PurchasePriceUnit | string |  |
| PurchasePriceQuantity | integer (int32) |  |
| Status | [PurchaseOrderLineStatus](#purchaseorderlinestatus) |  |
| SupplierReference | string |  |
| WarehouseCode | integer (int32) |  |
| OrderedQuantity | number (double) |  |
| DeliveredQuantity | number (double) |  |
| OrderType | integer (int32) |  |
| PurchaseOrder | [PurchaseOrderContract](#purchaseordercontract) |  |
| Product | [ProductContract](#productcontract) |  |
| SalesOrder | [SalesOrderContract](#salesordercontract) |  |
| SalesOrderLine | [SalesOrderLineContract](#salesorderlinecontract) |  |
| WorkOrderLine | [WorkOrderLineContract](#workorderlinecontract) |  |

### Model: PurchaseOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseOrderLineContract[]](#purchaseorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [PurchaseOrderLineContract](#purchaseorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: PurchaseOrderLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |
| SalesOrder | [SalesOrderIncludes](#salesorderincludes) |  |
| SalesOrderLine | [SalesOrderLineIncludes](#salesorderlineincludes) |  |
| WorkOrderLine | [WorkOrderLineIncludes](#workorderlineincludes) |  |
| PurchaseOrder | [PurchaseOrderIncludes](#purchaseorderincludes) |  |

### Model: PurchaseOrderLineStatus

string

### Model: PurchaseOrderStatus

string

### Model: QuantityDiscountContract


| Field | Type | Description |
| --- | --- | --- |
| Quantity | number (double) |  |
| GrossPriceExVat | number (double) |  |
| GrossPriceIncVat | number (double) |  |
| CustomerGrossPriceExVat | number (double) |  |
| CustomerGrossPriceIncVat | number (double) |  |
| NetPriceExVat | number (double) |  |
| NetPriceIncVat | number (double) |  |

### Model: QuantityDiscountContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [QuantityDiscountContract[]](#quantitydiscountcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: QuantityDiscountContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [QuantityDiscountContract](#quantitydiscountcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: QueryFilter

object

### Model: RelationContract


| Field | Type | Description |
| --- | --- | --- |
| Name1 | string |  |
| Name2 | string |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| CountryCode | integer (int32) |  |
| Phone | string |  |
| MobilePhone | string |  |
| EmailAddress | string |  |
| InvoiceEmailAddress | string |  |
| KvkNumber | string |  |
| ContactPerson | string |  |
| VatRegistrationNumber | string |  |
| WebsiteUrl | string |  |
| DebtorDiscountGroup | string |  |
| MailCode1 | string |  |
| MailCode2 | string |  |
| MailCode3 | string |  |
| MailCode4 | string |  |
| MailCode5 | string |  |
| MailCode6 | string |  |
| PayVat | boolean |  |
| Type | [RelationType](#relationtype) |  |
| DebtorPaymentConditionCode | integer (int32) |  |
| DebtorDeliveryConditionCode | integer (int32) |  |
| DebtorVatCode | integer (int32) |  |
| GlobalLocationNumber | string |  |
| InternationalBankAccountNumber | string |  |
| Id | string (uuid) |  |
| RelationCode | integer (int32) |  |
| InvoiceRelationCode | integer (int32) |  |
| DebtorDiscountPercentage | number (double) |  |
| IsDebtor | boolean |  |
| IsCreditor | boolean |  |
| Active | boolean |  |
| DebtorCurrencyCode | integer (int32) |  |
| AcceptOrdersForDebtor | [AcceptOrdersForDebtor](#acceptordersfordebtor) |  |
| DebtorExpeditionCode | integer (int32) |  |
| CreditorDeliveryDays | integer (int32) |  |
| CreditorVatCode | integer (int32) |  |
| CreditorPaymentConditionCode | integer (int32) |  |
| UseDefaultEmailAddressByEDocument | boolean |  |
| LastModified | string (date-time) | Format: yyyy-MM-dd |
| EDocumentEmailAddresses | [EDocumentEmailAddressContract[]](#edocumentemailaddresscontract) |  |
| DeliveryAddresses | [DeliveryAddressContract[]](#deliveryaddresscontract) |  |
| VatInformation | [VatInformationContract](#vatinformationcontract) |  |
| DebtorDeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |
| DebtorPaymentCondition | [PaymentConditionContract](#paymentconditioncontract) |  |
| Country | [CountryContract](#countrycontract) |  |
| DebtorCurrency | [CurrencyContract](#currencycontract) |  |
| ContactPersons | [ContactPersonContract[]](#contactpersoncontract) |  |

### Model: RelationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [RelationContract[]](#relationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: RelationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [RelationContract](#relationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: RelationIncludes


| Field | Type | Description |
| --- | --- | --- |
| Country | [CountryIncludes](#countryincludes) |  |
| VatInformation | [EmptyIncludes](#emptyincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |
| PaymentCondition | [EmptyIncludes](#emptyincludes) |  |
| Currency | [EmptyIncludes](#emptyincludes) |  |
| DeliveryAddresses | [DeliveryAddressIncludes](#deliveryaddressincludes) |  |
| EDocumentEmailAddresses | [EmptyIncludes](#emptyincludes) |  |
| ContactPersons | [EmptyIncludes](#emptyincludes) |  |

### Model: RelationType

string

### Model: SalesOrderContract


| Field | Type | Description |
| --- | --- | --- |
| OrderType | integer (int32) |  |
| InvoiceName1 | string |  |
| InvoiceName2 | string |  |
| InvoiceAddressLine | string |  |
| InvoiceZipCode | string |  |
| InvoiceTown | string |  |
| InvoiceCountryCode | integer (int32) |  |
| DeliveryName1 | string |  |
| DeliveryName2 | string |  |
| DeliveryAddressLine | string |  |
| DeliveryZipCode | string |  |
| DeliveryTown | string |  |
| DeliveryCountryCode | integer (int32) |  |
| Reference1 | string |  |
| Reference2 | string |  |
| SellerCode | integer (int32) |  |
| CostCenterCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| PaymentConditionCode | integer (int32) |  |
| ExpeditionCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| RayonCode | string |  |
| SelectionCode | string |  |
| ContactPersonCode | integer (int32) |  |
| AllowPartialDelivery | boolean |  |
| AllowPartialInvoicing | boolean |  |
| TrackAndTraceNumber | string |  |
| Remark | string |  |
| EmailAddress | string |  |
| Phone | string |  |
| ServicePointId | integer (int32) |  |
| ApprovalCode | string |  |
| Id | string (uuid) |  |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| OrderDate | string (date-time) | Format: yyyy-MM-dd |
| DiscountPercentage | number (double) |  |
| ExpectedDeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| Status | [SalesOrderStatus](#salesorderstatus) |  |
| DeliveryAddressId | string (uuid) |  |
| DeliverySequenceNumber | integer (int32) |  |
| LastModified | string (date-time) | Format: yyyy-MM-dd |
| TotalGrossPriceExVat | number (double) |  |
| TotalGrossPriceIncVat | number (double) |  |
| TotalNetPriceExVat | number (double) |  |
| TotalNetPriceIncVat | number (double) |  |
| InvoiceCountry | [CountryContract](#countrycontract) |  |
| DeliveryCountry | [CountryContract](#countrycontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| Seller | [EmployeeContract](#employeecontract) |  |
| PaymentCondition | [PaymentConditionContract](#paymentconditioncontract) |  |
| DeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |
| PreInvoices | [PreInvoiceContract[]](#preinvoicecontract) |  |
| Lines | [SalesOrderLineContract[]](#salesorderlinecontract) |  |

### Model: SalesOrderContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SalesOrderContract[]](#salesordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SalesOrderContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SalesOrderContract](#salesordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SalesOrderIncludes


| Field | Type | Description |
| --- | --- | --- |
| Relation | [RelationIncludes](#relationincludes) |  |
| Seller | [EmptyIncludes](#emptyincludes) |  |
| Country | [CountryIncludes](#countryincludes) |  |
| TotalPrices | [EmptyIncludes](#emptyincludes) |  |
| Lines | [SalesOrderLineIncludes](#salesorderlineincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |
| PaymentCondition | [EmptyIncludes](#emptyincludes) |  |

### Model: SalesOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| LineNumber | integer (int32) | Either leave empty, or provide a contiguous sequence for explicit ordering |
| QuantityOrdered | number (double) |  |
| Description | string |  |
| ExtendedDescription | string |  |
| CustomerReference | string |  |
| DiscountPercentage | number (double) | Fill in with the AppliedDiscountPercentage from /products/prices, or leave empty, so that the API will calculate it for you |
| DeliveryDate | string (date-time) | Format: yyyy-MM-dd |
| InvoiceLineCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| Id | string (uuid) |  |
| RecordNumber | integer (int32) |  |
| SalesOrderId | string (uuid) |  |
| RelationId | string (uuid) |  |
| Type | [SalesOrderLineType](#salesorderlinetype) |  |
| ProductCode | string |  |
| ServiceNumber | integer (int32) |  |
| VatCode | integer (int32) |  |
| VatPercentage | number (double) |  |
| QuantityAllocated | number (double) |  |
| QuantityPicked | number (double) |  |
| QuantityInvoiced | number (double) |  |
| PurchaseEntryNumber | integer (int32) |  |
| CollectStatus | string |  |
| GrossPriceExVat | number (double) |  |
| GrossPriceIncVat | number (double) |  |
| NetPriceExVat | number (double) |  |
| NetPriceIncVat | number (double) |  |
| Product | [ProductContract](#productcontract) |  |
| ServiceObject | [ServiceObjectContract](#serviceobjectcontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| SalesOrder | [SalesOrderContract](#salesordercontract) |  |
| DeliveryLines | [DeliveryLineContract[]](#deliverylinecontract) |  |
| PreInvoiceLines | [PreInvoiceLineContract[]](#preinvoicelinecontract) |  |

### Model: SalesOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SalesOrderLineContract[]](#salesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SalesOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SalesOrderLineContract](#salesorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SalesOrderLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |
| ServiceObject | [ServiceObjectIncludes](#serviceobjectincludes) |  |
| Relation | [RelationIncludes](#relationincludes) |  |
| SalesOrder | [SalesOrderIncludes](#salesorderincludes) |  |
| DeliveryLines | [DeliveryLineIncludes](#deliverylineincludes) |  |

### Model: SalesOrderLineType

string

### Model: SalesOrderStatus

string

### Model: Scope

string

### Model: ServiceMessageCategoryContract


| Field | Type | Description |
| --- | --- | --- |
| MainCategory | integer (int32) |  |
| SubCategory | integer (int32) |  |
| ShortDescription | string |  |
| Description | string |  |

### Model: ServiceMessageCategoryContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceMessageCategoryContract[]](#servicemessagecategorycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceMessageCategoryContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceMessageCategoryContract](#servicemessagecategorycontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceMessageContract


| Field | Type | Description |
| --- | --- | --- |
| MainCategoryId | integer (int32) |  |
| SubCategoryId | integer (int32) |  |
| CreatorEmployeeId | integer (int32) |  |
| DestinationEmployeeId | integer (int32) |  |
| ServiceObjectDescription | string |  |
| ServiceObjectSerialNumber | string |  |
| ServiceObjectRegistrationNumber | string |  |
| ServiceObjectCustomerRegCode | string |  |
| Name | string |  |
| CountryCode | integer (int32) |  |
| AddressLine | string |  |
| ZipCode | string |  |
| Town | string |  |
| RayonCode | string |  |
| ContactPersonName | string |  |
| ContactPersonEmailAddress | string |  |
| ContactPersonPhone | string |  |
| Subject | string |  |
| OrderData | string |  |
| Priority | [ServiceMessagePriority](#servicemessagepriority) |  |
| RequestDate | string (date-time) | Format: yyyy-MM-dd |
| CreationDate | string (date-time) | Format: yyyy-MM-dd |
| CostCenterCode | integer (int32) |  |
| TravelZoneCode | integer (int32) |  |
| Text | string |  |
| TransferNumber | integer (int32) |  |
| TransferLineNumber | integer (int32) |  |
| Id | string (uuid) |  |
| MessageNumber | integer (int32) |  |
| DateCreated | string (date-time) | Format: yyyy-MM-dd |
| DateLastModified | string (date-time) | Format: yyyy-MM-dd |
| ServiceObjectId | string (uuid) |  |
| ServiceNumber | integer (int32) |  |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| Status | [ServiceMessageStatus](#servicemessagestatus) |  |
| Relation | [RelationContract](#relationcontract) |  |

### Model: ServiceMessageContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceMessageContract[]](#servicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceMessageContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceMessageContract](#servicemessagecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceMessagePriority

string

### Model: ServiceMessageStatus

string

### Model: ServiceObjectContract


| Field | Type | Description |
| --- | --- | --- |
| Inspection1StickerNumber | string |  |
| Inspection1LastDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection1NextDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection2StickerNumber | string |  |
| Inspection2LastDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection2NextDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection3StickerNumber | string |  |
| Inspection3LastDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection3NextDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection4StickerNumber | string |  |
| Inspection4LastDate | string (date-time) | Format: yyyy-MM-dd |
| Inspection4NextDate | string (date-time) | Format: yyyy-MM-dd |
| Counter1 | integer (int32) |  |
| InUseDate | string (date-time) | Format: yyyy-MM-dd |
| WarrantyDate | string (date-time) | Format: yyyy-MM-dd |
| CustomerRegCode | string |  |
| ServiceNumber | integer (int32) |  |
| MainGroupCode | string |  |
| SubGroupCode | string |  |
| FinancialGroup | integer (int32) |  |
| BuildYear | integer (int32) |  |
| Type | string |  |
| ProductCode | string |  |
| RegistrationNumber | string |  |
| ForeignRegistrationNumber | boolean |  |
| MakeCode | integer (int32) |  |
| MakeDescription | string |  |
| Description1 | string |  |
| Description2 | string |  |
| Description3 | string |  |
| Description4 | string |  |
| Description5 | string |  |
| Description6 | string |  |
| SerialNumber1 | string |  |
| SerialNumber2 | string |  |
| SerialNumber3 | string |  |
| PurchaseStatus | [ServiceObjectPurchaseStatus](#serviceobjectpurchasestatus) |  |
| PurchasePrice | number (double) |  |
| SalesStatus | [ServiceObjectSalesStatus](#serviceobjectsalesstatus) |  |
| SalesRelationCode | integer (int32) |  |
| SalesPrice | number (double) |  |
| AdvicePrice | number (double) |  |
| TradePrice | number (double) |  |
| Counter2 | integer (int32) |  |
| SalesOrderDate | string (date-time) | Format: yyyy-MM-dd |
| UserRelationCode | integer (int32) |  |
| Inspection1FrequencyInDays | integer (int32) |  |
| Inspection2FrequencyInDays | integer (int32) |  |
| Inspection3FrequencyInDays | integer (int32) |  |
| Inspection4FrequencyInDays | integer (int32) |  |
| DateCreated | string (date-time) | Format: yyyy-MM-dd |
| VatType | [ServiceObjectVatType](#serviceobjectvattype) |  |
| UserStatus | [ServiceObjectUserStatus](#serviceobjectuserstatus) |  |
| ShowOnWebsite1 | boolean |  |
| ShowOnWebsite2 | boolean |  |
| ShowOnWebsite3 | boolean |  |
| ShowOnWebsite4 | boolean |  |
| ShowOnWebsite5 | boolean |  |
| ShowOnWebsite6 | boolean |  |
| ShowOnWebsite7 | boolean |  |
| ShowOnWebsite8 | boolean |  |
| ShowOnWebsite9 | boolean |  |
| Color | string |  |
| SellerCode | integer (int32) |  |
| Location | string |  |
| SalesOrderNumber | integer (int32) |  |
| InvoiceNumber | integer (int32) |  |
| InvoiceDate | string (date-time) | Format: yyyy-MM-dd |
| ShowOnWebsite10 | boolean |  |
| ShowOnWebsite11 | boolean |  |
| ShowOnWebsite12 | boolean |  |
| ShowOnWebsite13 | boolean |  |
| ShowOnWebsite14 | boolean |  |
| ShowOnWebsite15 | boolean |  |
| ShowOnWebsite16 | boolean |  |
| ShowOnWebsite17 | boolean |  |
| ShowOnWebsite18 | boolean |  |
| ShowOnWebsite19 | boolean |  |
| ShowOnWebsite20 | boolean |  |
| PriceType | [ServiceObjectPriceType](#serviceobjectpricetype) |  |
| DateLastMutated | string (date-time) | Format: yyyy-MM-dd |
| SelectionCode1 | string |  |
| SelectionCode2 | string |  |
| SelectionCode3 | string |  |
| SelectionCode4 | string |  |
| SelectionCode5 | string |  |
| SelectionCode6 | string |  |
| SelectionCode7 | string |  |
| SelectionCode8 | string |  |
| PurchaseRelationCode | integer (int32) |  |
| PurchaseOrderDate | string (date-time) | Format: yyyy-MM-dd |
| ShowPriceIncVat | boolean |  |
| PurchaseOrigin | [ServiceObjectPurchaseOrigin](#serviceobjectpurchaseorigin) |  |
| ConfigurationElements | [ConfigurationElementContract[]](#configurationelementcontract) |  |
| Seller | [EmployeeContract](#employeecontract) |  |
| SalesRelation | [RelationContract](#relationcontract) |  |
| UserRelation | [RelationContract](#relationcontract) |  |
| PurchaseRelation | [RelationContract](#relationcontract) |  |
| MainGroup | [ServiceObjectGroupContract](#serviceobjectgroupcontract) |  |
| SubGroup | [ServiceObjectGroupContract](#serviceobjectgroupcontract) |  |
| Product | [ProductContract](#productcontract) |  |
| DossierItems | [DossierItemContract[]](#dossieritemcontract) |  |
| WebsiteInformation | [ServiceObjectWebsiteInformationContract[]](#serviceobjectwebsiteinformationcontract) |  |

### Model: ServiceObjectContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectContract[]](#serviceobjectcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectContract](#serviceobjectcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectGroupContract


| Field | Type | Description |
| --- | --- | --- |
| MainGroupCode | string |  |
| SubGroupCode | string |  |
| Description | string |  |
| Visible | boolean |  |
| IsStandard | boolean |  |
| StandardGroup | [ServiceObjectStandardGroupContract](#serviceobjectstandardgroupcontract) |  |

### Model: ServiceObjectGroupContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectGroupContract[]](#serviceobjectgroupcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectGroupContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectGroupContract](#serviceobjectgroupcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectGroupIncludes


| Field | Type | Description |
| --- | --- | --- |
| StandardGroup | [EmptyIncludes](#emptyincludes) |  |

### Model: ServiceObjectIncludes


| Field | Type | Description |
| --- | --- | --- |
| ConfigurationElements | [ConfigurationElementIncludes](#configurationelementincludes) |  |
| Seller | [EmptyIncludes](#emptyincludes) |  |
| SalesRelation | [RelationIncludes](#relationincludes) |  |
| UserRelation | [RelationIncludes](#relationincludes) |  |
| PurchaseRelation | [RelationIncludes](#relationincludes) |  |
| Groups | [ServiceObjectGroupIncludes](#serviceobjectgroupincludes) |  |
| Product | [ProductIncludes](#productincludes) |  |
| DossierItems | [EmptyIncludes](#emptyincludes) |  |
| WebsiteInformation | [StringEmptyIncludesListIncludes](#stringemptyincludeslistincludes) |  |
| StickerNumbers | [EmptyIncludes](#emptyincludes) |  |

### Model: ServiceObjectLabelSendRequestContract


| Field | Type | Description |
| --- | --- | --- |
| EmailAddress | string |  |
| EmployeeCode | integer (int32) |  |
| Subject | string |  |
| Message | string |  |
| YourPrice | number (double) |  |

### Model: ServiceObjectLabelSendRequestContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectLabelSendRequestContract[]](#serviceobjectlabelsendrequestcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectLabelSendRequestContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectLabelSendRequestContract](#serviceobjectlabelsendrequestcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectPriceType

string

### Model: ServiceObjectPurchaseOrigin

string

### Model: ServiceObjectPurchaseStatus

string

### Model: ServiceObjectSalesStatus

string

### Model: ServiceObjectStandardGroupContract


| Field | Type | Description |
| --- | --- | --- |
| MainGroupCode | string |  |
| SubGroupCode | string |  |
| Description | string |  |

### Model: ServiceObjectStandardGroupContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectStandardGroupContract[]](#serviceobjectstandardgroupcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectStandardGroupContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectStandardGroupContract](#serviceobjectstandardgroupcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeContract


| Field | Type | Description |
| --- | --- | --- |
| Make | string |  |
| Model | string |  |
| Year | integer (int32) |  |
| Slug | string |  |
| PromotionalInformation | [ServiceObjectTypePromotionalInformationContract](#serviceobjecttypepromotionalinformationcontract) |  |

### Model: ServiceObjectTypeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeContract[]](#serviceobjecttypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeContract](#serviceobjecttypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeProductSlugLinkContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Slug | string |  |

### Model: ServiceObjectTypeProductSlugLinkContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeProductSlugLinkContract[]](#serviceobjecttypeproductsluglinkcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeProductSlugLinkContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeProductSlugLinkContract](#serviceobjecttypeproductsluglinkcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypePromotionalInformationContract


| Field | Type | Description |
| --- | --- | --- |
| ImageUrl | string |  |
| Description | string |  |

### Model: ServiceObjectTypePromotionalInformationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypePromotionalInformationContract[]](#serviceobjecttypepromotionalinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypePromotionalInformationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypePromotionalInformationContract](#serviceobjecttypepromotionalinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeSuggestionContract


| Field | Type | Description |
| --- | --- | --- |
| Description | string |  |
| Slug | string |  |

### Model: ServiceObjectTypeSuggestionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeSuggestionContract[]](#serviceobjecttypesuggestioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectTypeSuggestionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectTypeSuggestionContract](#serviceobjecttypesuggestioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectUserStatus

string

### Model: ServiceObjectVatType

string

### Model: ServiceObjectWebsiteInformationContract


| Field | Type | Description |
| --- | --- | --- |
| IsoLanguageCode | string |  |
| Description | string |  |
| Configuration | string |  |

### Model: ServiceObjectWebsiteInformationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectWebsiteInformationContract[]](#serviceobjectwebsiteinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: ServiceObjectWebsiteInformationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [ServiceObjectWebsiteInformationContract](#serviceobjectwebsiteinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: StringEmptyIncludesListIncludes


| Field | Type | Description |
| --- | --- | --- |
| ValueList | string[] |  |
| IncludeObject | [EmptyIncludes](#emptyincludes) |  |

### Model: SupplierIncludes


| Field | Type | Description |
| --- | --- | --- |
| Relation | [RelationIncludes](#relationincludes) |  |

### Model: SuppressionType

string

### Model: SyncAction

string

### Model: SyncActionContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |
| Type | [SyncActionType](#syncactiontype) |  |
| Action | [SyncAction](#syncaction) |  |
| TargetId | string (uuid) |  |
| DateCreated | string (date-time) | Format: yyyy-MM-dd |
| DateLastModified | string (date-time) | Format: yyyy-MM-dd |
| Status | [ProcessStatus](#processstatus) |  |
| Tries | integer (int32) |  |
| Logs | [ConnectApiLogContract[]](#connectapilogcontract) |  |

### Model: SyncActionContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SyncActionContract[]](#syncactioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SyncActionContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [SyncActionContract](#syncactioncontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: SyncActionType

string

### Model: TaskTypeContract


| Field | Type | Description |
| --- | --- | --- |
| Id | integer (int32) |  |
| Description | string |  |

### Model: TaskTypeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [TaskTypeContract[]](#tasktypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: TaskTypeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [TaskTypeContract](#tasktypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: VatCodeContract


| Field | Type | Description |
| --- | --- | --- |
| VatCode | integer (int32) |  |
| Type | string |  |
| Active | boolean |  |
| Percentage01 | number (double) |  |
| Percentage02 | number (double) |  |
| Percentage03 | number (double) |  |
| Percentage04 | number (double) |  |
| Percentage05 | number (double) |  |
| Percentage06 | number (double) |  |
| Percentage07 | number (double) |  |
| Percentage08 | number (double) |  |
| Percentage09 | number (double) |  |
| Percentage10 | number (double) |  |
| EffectiveDate01 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate02 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate03 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate04 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate05 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate06 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate07 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate08 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate09 | string (date-time) | Format: yyyy-MM-dd |
| EffectiveDate10 | string (date-time) | Format: yyyy-MM-dd |
| Description | string |  |
| EffectivePercentage | number (double) |  |

### Model: VatCodeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [VatCodeContract[]](#vatcodecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: VatCodeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [VatCodeContract](#vatcodecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: VatInformationContract


| Field | Type | Description |
| --- | --- | --- |
| VatCode | integer (int32) |  |
| VatPercentage | number (double) |  |
| Description | string |  |

### Model: VatInformationContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [VatInformationContract[]](#vatinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: VatInformationContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [VatInformationContract](#vatinformationcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WarehouseContract


| Field | Type | Description |
| --- | --- | --- |
| WarehouseCode | integer (int32) |  |
| Description | string |  |

### Model: WarehouseContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WarehouseContract[]](#warehousecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WarehouseContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WarehouseContract](#warehousecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderContract


| Field | Type | Description |
| --- | --- | --- |
| Id | string (uuid) |  |
| RelationId | string (uuid) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| Status | [WorkOrderStatus](#workorderstatus) |  |
| ApprovalCode | string |  |
| SelectionCode | string |  |
| IsInternal | boolean |  |
| OrderDate | string (date-time) | Format: yyyy-MM-dd |
| ServiceNumber | integer (int32) |  |
| Reference1 | string |  |
| Reference2 | string |  |
| SellerCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| CostCenterCode | integer (int32) |  |
| InvoiceRelationCode | integer (int32) |  |
| InvoiceName1 | string |  |
| InvoiceName2 | string |  |
| InvoiceAddressLine | string |  |
| InvoiceZipCode | string |  |
| InvoiceTown | string |  |
| InvoiceCountryCode | integer (int32) |  |
| DeliverySequenceNumber | integer (int32) |  |
| DeliveryName1 | string |  |
| DeliveryName2 | string |  |
| DeliveryAddressLine | string |  |
| DeliveryZipCode | string |  |
| DeliveryTown | string |  |
| DeliveryCountryCode | integer (int32) |  |
| DeliveryContactPersonCode | integer (int32) |  |
| PaymentConditionCode | integer (int32) |  |
| DeliveryConditionCode | integer (int32) |  |
| ExpeditionCode | integer (int32) |  |
| TotalNetPriceExVat | number (double) |  |
| TotalNetPriceIncVat | number (double) |  |
| HoursAmountIncVat | number (double) |  |
| HoursAmountExVat | number (double) |  |
| HoursQuantity | number (double) |  |
| FixedAmount | number (double) |  |
| WorkOrderTypeCode | integer (int32) |  |
| InvoiceCountry | [CountryContract](#countrycontract) |  |
| DeliveryCountry | [CountryContract](#countrycontract) |  |
| ServiceObject | [ServiceObjectContract](#serviceobjectcontract) |  |
| Relation | [RelationContract](#relationcontract) |  |
| InvoiceRelation | [RelationContract](#relationcontract) |  |
| Seller | [EmployeeContract](#employeecontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |
| CostCenter | [CostCenterContract](#costcentercontract) |  |
| WorkOrderType | [WorkOrderTypeContract](#workordertypecontract) |  |
| TaskDescription | string |  |
| InternalNotes | [WorkOrderInternalNoteContract[]](#workorderinternalnotecontract) |  |
| PaymentCondition | [PaymentConditionContract](#paymentconditioncontract) |  |
| DeliveryCondition | [DeliveryConditionContract](#deliveryconditioncontract) |  |
| Lines | [WorkOrderLineContract[]](#workorderlinecontract) |  |
| Hours | [WorkOrderHourContract[]](#workorderhourcontract) |  |
| PreInvoice | [PreInvoiceContract](#preinvoicecontract) |  |

### Model: WorkOrderContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderContract[]](#workordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderContract](#workordercontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderHourContract


| Field | Type | Description |
| --- | --- | --- |
| WorkDate | string (date-time) | Format: yyyy-MM-dd |
| EmployeeCode | integer (int32) |  |
| TaskTypeId | integer (int32) |  |
| Description | string |  |
| StartTime | string (date-span) |  |
| EndTime | string (date-span) |  |
| BreakTimeMinutes | integer (int32) |  |
| ActualHours | number (double) | Required when no start or end time is specified. |
| InvoiceHours | number (double) |  |
| Percentage | number (double) |  |
| Price | number (double) |  |
| InvoiceLineCode | integer (int32) |  |
| Id | string (uuid) |  |
| RecordNumber | integer (int32) |  |
| RelationCode | integer (int32) |  |
| EntryNumber | integer (int32) |  |
| LineNumber | integer (int32) |  |
| Employee | [EmployeeContract](#employeecontract) |  |
| TaskType | [TaskTypeContract](#tasktypecontract) |  |

### Model: WorkOrderHourContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderHourContract[]](#workorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderHourContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderHourContract](#workorderhourcontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderHourIncludes


| Field | Type | Description |
| --- | --- | --- |
| Employee | [EmptyIncludes](#emptyincludes) |  |
| TaskType | [EmptyIncludes](#emptyincludes) |  |

### Model: WorkOrderIncludes


| Field | Type | Description |
| --- | --- | --- |
| ServiceObject | [ServiceObjectIncludes](#serviceobjectincludes) |  |
| Relation | [RelationIncludes](#relationincludes) |  |
| InvoiceRelation | [RelationIncludes](#relationincludes) |  |
| Country | [CountryIncludes](#countryincludes) |  |
| Seller | [EmptyIncludes](#emptyincludes) |  |
| Warehouse | [EmptyIncludes](#emptyincludes) |  |
| CostCenter | [EmptyIncludes](#emptyincludes) |  |
| TaskDescription | [EmptyIncludes](#emptyincludes) |  |
| InternalNotes | [EmptyIncludes](#emptyincludes) |  |
| WorkOrderType | [EmptyIncludes](#emptyincludes) |  |
| DeliveryCondition | [EmptyIncludes](#emptyincludes) |  |
| PaymentCondition | [EmptyIncludes](#emptyincludes) |  |
| Lines | [WorkOrderLineIncludes](#workorderlineincludes) |  |
| Hours | [WorkOrderHourIncludes](#workorderhourincludes) |  |
| PreInvoice | [PreInvoiceIncludes](#preinvoiceincludes) |  |

### Model: WorkOrderInternalNoteContract


| Field | Type | Description |
| --- | --- | --- |
| EmployeeCode | integer (int32) |  |
| Text | string |  |
| Timestamp | string (date-time) | Format: yyyy-MM-dd |
| Employee | [EmployeeContract](#employeecontract) |  |

### Model: WorkOrderInternalNoteContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderInternalNoteContract[]](#workorderinternalnotecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderInternalNoteContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderInternalNoteContract](#workorderinternalnotecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderLineContract


| Field | Type | Description |
| --- | --- | --- |
| ProductCode | string |  |
| Description | string |  |
| QuantityOrdered | number (double) |  |
| QuantityDelivered | number (double) |  |
| DiscountPercentage | number (double) |  |
| VatCode | integer (int32) |  |
| InvoiceLineCode | integer (int32) |  |
| WarehouseCode | integer (int32) |  |
| RecordNumber | integer (int32) |  |
| LineNumber | integer (int32) |  |
| Type | [WorkOrderLineType](#workorderlinetype) |  |
| GrossPriceExVat | number (double) |  |
| GrossPriceIncVat | number (double) |  |
| NetPriceExVat | number (double) |  |
| NetPriceIncVat | number (double) |  |
| VatPercentage | number (double) |  |
| FinancialGroup | integer (int32) |  |
| Product | [ProductContract](#productcontract) |  |
| Warehouse | [WarehouseContract](#warehousecontract) |  |

### Model: WorkOrderLineContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderLineContract[]](#workorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderLineContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderLineContract](#workorderlinecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderLineIncludes


| Field | Type | Description |
| --- | --- | --- |
| Product | [ProductIncludes](#productincludes) |  |
| Warehouse | [EmptyIncludes](#emptyincludes) |  |

### Model: WorkOrderLineType

string

### Model: WorkOrderStatus

string

### Model: WorkOrderTypeContract


| Field | Type | Description |
| --- | --- | --- |
| OrderType | integer (int32) |  |
| Description | string |  |

### Model: WorkOrderTypeContractListResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderTypeContract[]](#workordertypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

### Model: WorkOrderTypeContractResponseWrapperContract


| Field | Type | Description |
| --- | --- | --- |
| Data | [WorkOrderTypeContract](#workordertypecontract) |  |
| Error |  |  |
| TotalItems | integer (int64) |  |

