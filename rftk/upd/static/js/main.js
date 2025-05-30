// Скрипт для копирования полей при выборе "Он же"
document.addEventListener("DOMContentLoaded", function () {
    function copyFields(fromPrefix, toPrefix, fields) {
        fields.forEach(field => {
            const fromInput = document.querySelector(`input[name="${fromPrefix}-${field}"]`);
            const toInput = document.querySelector(`input[name="${toPrefix}-${field}"]`);
            if (fromInput && toInput) {
                toInput.value = fromInput.value;
            }
        });
    }

    function clearFields(prefix, fields) {
        fields.forEach(field => {
            const input = document.querySelector(`input[name="${prefix}-${field}"]`);
            if (input) {
                input.value = "";
            }
        });
    }

    function handleRelationRadios(radioName, fromPrefix, toPrefix, fields) {
        const radios = document.querySelectorAll(`input[name="${radioName}"]`);
        radios.forEach(radio => {
            radio.addEventListener("change", function () {
                if (this.value === "Он же") {
                    copyFields(fromPrefix, toPrefix, fields);
                } else {
                    clearFields(toPrefix, fields);
                }
            });
        });
    }

    handleRelationRadios("shipper-relation_type", "seller", "shipper", ["name", "inn", "kpp", "address", "manager_fio"]);
    handleRelationRadios("consignee-relation_type", "buyer", "consignee", ["name", "inn", "kpp", "address", "manager_fio"]);
});

// Модальное окно для добавления раздела товара
document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("modal_window_product");
  const openBtn = document.getElementById("show-section-form");
  const closeBtn = document.getElementById("close-section-form");

  if (openBtn && modal) {
    openBtn.addEventListener("click", () => {
      modal.showModal();
    });
  }

  if (closeBtn && modal) {
    closeBtn.addEventListener("click", () => {
      modal.close();
    });
  }
});


// Добавление строк в блоках 3 и 8
function addPaymentDocumentRow() {
  const container = document.getElementById('payment-documents-container');
  const totalForms = document.getElementById('id_payment_document-TOTAL_FORMS');
  const formCount = parseInt(totalForms.value);
  
  const newRow = document.createElement('div');
  newRow.className = 'payment-document-row';
  newRow.innerHTML = `
        <form
          method="post"
          action="{% url 'index' %}"
          enctype="multipart/form-data"
          novalidate
        >
          {% csrf_token %}
      <td>{{ payment_document_form.number.label_tag }} {{ payment_document_form.number }}</td>
      <td>{{ payment_document_form.date.label_tag }} {{ payment_document_form.date }}</td>
      </form>`;
  
  container.appendChild(newRow);
  totalForms.value = formCount + 1;
}