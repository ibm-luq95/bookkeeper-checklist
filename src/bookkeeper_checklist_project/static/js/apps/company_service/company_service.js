"use strict";

import {
  fetchUrlPathByName,
  formInputSerializer,
  sendRequest,
} from "../../utils/helpers.js";
import { MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  //company_services:api:manager:create
  const modalId = "company-services-form-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const companyServiceForm = modalElement.querySelector("form");
  const fieldset = companyServiceForm.querySelector("fieldset");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const addServiceBtn = document.querySelector("button#addServiceBtn");

  // create new service button
  addServiceBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: async () => {
        modalTitleElement.textContent = "Create";
        submitButton.textContent = "Create";
        companyServiceForm.setAttribute("method", "POST");
        companyServiceForm["_method"].value = "POST";

        const createUrl = await fetchUrlPathByName(
          "company_services:api:create"
        );
        companyServiceForm.setAttribute("action", createUrl["urlPath"]);
      },
      onCloseCallback: () => {
        companyServiceForm["_method"].value = "";
      },
    };
    new MicroModalHandler(modalId, callBacks);
  });

  // add new company service form event
  companyServiceForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const formInputs = formInputSerializer({
      formElement: currentTarget,
      excludedFields: ["_method"],
    });
    // console.log(formInputs);
    const requestOptions = {
      method: currentTarget["_method"].value,
      dataToSend: formInputs,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification(data["msg"], "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(
          `${JSON.stringify(error["user_error_msg"])}`,
          "danger"
        );
      })
      .finally(() => {});
  });
});
