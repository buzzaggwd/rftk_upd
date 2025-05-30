from django import forms
from django.forms import widgets
from . import models
from django.forms import formset_factory


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = models.Invoice
        fields = "__all__"
        labels = {
            "invoice_number": "Счет-фактура №",
            "date": "от",
            "is_adjusted": "Исправления",
            "adjusted_number": "Исправление №",
            "adjusted_date": "от",
        }
        widgets = {
            "is_adjusted": forms.RadioSelect(
                choices=[(False, "Не вносились"), (True, "Вносились")]
            )
        }


class AdvancePaymentForm(forms.ModelForm):
    class Meta:
        model = models.AdvancePayment
        fields = "__all__"
        labels = {
            "is_advance": "На авансовый платеж",
        }
        widgets = {
            "is_advance": forms.RadioSelect(choices=[(True, "Да"), (False, "Нет")])
        }


class PaymentDocumentForm(forms.ModelForm):
    class Meta:
        model = models.PaymentDocument
        fields = "__all__"
        labels = {
            "number": "№ документа",
            "date": "Дата",
        }

PaymentDocumentFormSet = formset_factory(PaymentDocumentForm, extra=1)


class ShippingDocumentForm(forms.ModelForm):
    class Meta:
        model = models.ShippingDocument
        fields = "__all__"
        labels = {
            "name": "Наименование документа",
            "number": "№ документа",
            "date": "Дата",
        }


class SellerForm(forms.ModelForm):
    class Meta:
        model = models.Seller
        fields = "__all__"
        # exclude = ["type"]
        labels = {
            # type не передаем
            "status": "Статус:",
            "name": "Наименование:",
            "full_name": "Полное наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "reg_address": "Адрес регистрации:",
            "address": "Адрес:",
            "requisite": "Реквизиты св-ва ИП:",
            "manager": "Должность руководителя:",
            "manager_fio": "Руководитель Ф.И.О.:",
            "accountant_fio": "Бухгалтер Ф.И.О.:",
        }

        widgets = {
            "status": forms.RadioSelect(
                choices=[("Организация", "Организация"), ("ИП", "ИП")]
            )
        }

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.type = "seller"
    #     if commit:
    #         instance.save()
    #     return instance


class BuyerForm(forms.ModelForm):
    class Meta:
        model = models.Buyer
        fields = "__all__"
        # exclude = ["type"]
        labels = {
            "name": "Наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "address": "Адрес:",
            "manager": "Должность руководителя:",
            "manager_fio": "Ф.И.О. Руководителя:",
        }

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.type = "buyer"
    #     if commit:
    #         instance.save()
    #     return instance


class ShipperForm(forms.ModelForm):
    class Meta:
        model = models.Shipper
        fields = "__all__"
        exclude = ["seller_id"]
        labels = {
            "relation_type": "",
            "name": "Наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "address": "Адрес:",
            "manager_fio": "Руководитель Ф.И.О.:",
        }

        widgets = {
            "relation_type": forms.RadioSelect(
                choices=[
                    ("Он же", "Он же"),
                    ("Другая организация", "Другая организация"),
                    ("Не указывать", "Не указывать"),
                ]
            ),
        }

    # def save(self, commit=True, seller_id=None):
    #     instance = super().save(commit=False)
    #     # instance.shipping_type = "shipper"
    #     if seller_id:
    #         instance.seller_id = models.Seller.objects.get(id=seller_id)
    #     if commit:
    #         instance.save()
    #     return instance


class ConsigneeForm(forms.ModelForm):
    class Meta:
        model = models.Consignee
        fields = "__all__"
        exclude = ["buyer_id"]
        labels = {
            "relation_type": "",
            "name": "Наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "address": "Адрес:",
            "manager_fio": "Руководитель Ф.И.О.:",
        }

        widgets = {
            "relation_type": forms.RadioSelect(
                choices=[
                    ("Он же", "Он же"),
                    ("Другая организация", "Другая организация"),
                    ("Не указывать", "Не указывать"),
                ]
            ),
        }

    # def save(self, commit=True, buyer_id=None):
    #     instance = super().save(commit=False)
    #     instance.shipping_type = "consignee"
    #     if buyer_id:
    #         instance.buyer_id = models.Buyer.objects.get(id=buyer_id)
    #     if commit:
    #         instance.save()
    #     return instance


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = models.AdditionalInfo
        fields = "__all__"
        labels = {
            "contact_identifier": "Идентификатор гос. контракта:",
            "document_type": "Тип документа:",
            "vat_rate": "Ставка НДС:",
            "nds_activ": "",
            "currency": "Валюта:",
            "form_format": "Печатная форма:",
        }

        widgets = {
            "document_type": forms.Select(
                choices=[
                    ("1", "1 - счет-фактура и передаточный документ(акт)"),
                    ("2", "2 - передаточный документ(акт)"),
                ]
            ),
            "vat_rate": forms.Select(
                choices=[
                    ("без НДС", "без НДС"),
                    ("0%", "0%"),
                    ("5%", "5%"),
                    ("7%", "7%"),
                    ("10%", "10%"),
                    ("18%", "18%"),
                    ("20%", "20%"),
                    ("разный", "разный"),
                ]
            ),
            "nds_activ": forms.RadioSelect(
                choices=[
                    ("не учитывать", "не учитывать"),
                    ("в сумме", "в сумме"),
                    ("сверху", "сверху"),
                ]
            ),
            "currency": forms.Select(
                choices=[
                    ("Российский рубль", "Российский рубль, 643"),
                    ("Доллар США", "Доллар США, 840"),
                    ("Евро", "Евро, 978"),
                    ("Белорусский рубль", "Белорусский рубль, 974"),
                    ("Гривна", "Гривна, 980"),
                    ("Тенге", "Тенге, 398"),
                    ("Бат", "Бат, 764"),
                    ("Новый туркменский манат", "Новый туркменский манат, 934"),
                    ("Условная единица", "Условная единица, 000"),
                ]
            ),
            "form_format": forms.Select(
                choices=[
                    ("УПД с 01.10.2024 г.", "УПД с 01.10.2024 г."),
                    (
                        "УПД с 01.10.2024 г. (версия 2)",
                        "УПД с 01.10.2024 г. (версия 2)",
                    ),
                    ("УПД с 01.07.2021 г.", "УПД с 01.07.2021 г."),
                    ("УПД с 01.07.2021 г. (1C)", "УПД с 01.07.2021 г. (1C)"),
                ]
            ),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = "__all__"
        labels = {
            "name": "Наименование:",
        }


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = "По умолчанию"
        self.fields['full_sum'].initial = 0.0
    
    class Meta:
        model = models.Product
        fields = "__all__"
        # exclude = ["section_id"]
        labels = {
            "section_id": "Раздел:",
            "name": "Наименование:",
            "article": "Артикул:",
            "unit": "Например: шт.",
            "quantity": "Код",
            "customs_code": "Код товара/работ, услуг:",
            "customs_type_code": "Код вида товара:",
            "excise_duty": "Акциз:",
            "number": "Кол-во",
            "country_code": "Цифровой код:",
            "country_name": "Краткое наименование:",
            "full_sum": "Сумма:",
            "customs_declaration_num": "Номер таможенной декларации:",
            "price": "Цена:",
        }

        # widgets = {
        #     'section': forms.HiddenInput()
        # }


class InfoBlockForm(forms.ModelForm):
    class Meta:
        model = models.InfoBlock
        fields = "__all__"
        labels = {
            "basis": "Основание передачи (сдачи) / получения (приемки):",
            "transportation_data": "Данные о транспортировке и грузе:",
        }


class TransferedForm(forms.ModelForm):
    class Meta:
        model = models.Transfered
        fields = "__all__"
        labels = {
            # type не передаем
            "position": "Должность:",
            "name": "Ф.И.О:",
            "date": "",  # Дата отгрузки (передачи): Дата получения (приемки):
            "is_signed": "Дата получения (приемки) совпадает с датой отгрузки",
            "other": "Иные сведения об отгрузке, передаче:",  # Иные сведения о получении, приемке:
            "resp_position": "Должность:",
            "resp_name": "Ф.И.О:",
        }

        widgets = {
            "is_signed": forms.CheckboxInput(),
        }


class ReceivedForm(forms.ModelForm):
    class Meta:
        model = models.Received
        fields = "__all__"
        labels = {
            # type не передаем
            "position": "Должность:",
            "name": "Ф.И.О:",
            "date": "",  # Дата отгрузки (передачи): Дата получения (приемки):
            "other": "Иные сведения об отгрузке, передаче:",  # Иные сведения о получении, приемке:
            "resp_position": "Должность:",
            "resp_name": "Ф.И.О:",
        }

        widgets = {
            "is_signed": forms.CheckboxInput(),
        }


class DocumentSellerForm(forms.ModelForm):
    class Meta:
        model = models.DocumentSeller
        fields = "__all__"
        labels = {
            "name": "Наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "type": "",
        }

        widgets = {
            "type": forms.RadioSelect(
                choices=[
                    ("Не указывать", "Не указывать"),
                    ("Продавец", "Продавец"),
                    ("Иное", "Иное"),
                ]
            ),
        }


class DocumentBuyerForm(forms.ModelForm):
    class Meta:
        model = models.DocumentBuyer
        fields = "__all__"
        labels = {
            "name": "Наименование:",
            "inn": "ИНН:",
            "kpp": "КПП:",
            "type": "",
        }

        widgets = {
            "type": forms.RadioSelect(
                choices=[
                    ("Не указывать", "Не указывать"),
                    ("Покупатель", "Покупатель"),
                    ("Иное", "Иное"),
                ]
            ),
        }


class OutputSettingsForm(forms.ModelForm):
    class Meta:
        model = models.OutputSettings
        fields = "__all__"
        labels = {
            "show_stamp": "Показать панель отправки документа по электронной почте (поставьте здесь галочку, чтобы созданный документ открылся с панелью отсылки по e-mail).",
            "show_signature": "Печать и подпись",
            "file_format": "",  # PDF (Portable Document Format) XLSX (Microsoft Office)
        }

        widgets = {
            "show_stamp": forms.CheckboxInput(),
            "show_signature": forms.CheckboxInput(),
            "file_format": forms.Select(
                choices=[
                    ("PDF", "PDF (Portable Document Format)"),
                    ("XLSX", "XLSX (Microsoft Office)"),
                ]
            ),
        }
