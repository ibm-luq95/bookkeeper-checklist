"use strict";
import {
  fetchUrlPathByName,
  formInputSerializer,
  sendRequest,
} from "../../utils/helpers.js";
import { MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const modalId = "important-contact-form-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const formElement = modalElement.querySelector("form");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const addContactBtn = document.querySelector("button#addContactBtn");

  addContactBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: async () => {
        modalTitleElement.textContent = "Create new contact";
        submitButton.textContent = "Create";
        formElement.setAttribute("method", "POST");
        formElement["_method"].value = "POST";

        const createUrl = await fetchUrlPathByName(
          "important_contact:api:create"
        );
        formElement.setAttribute("action", createUrl["urlPath"]);
      },
      onCloseCallback: () => {
        formElement["_method"].value = "";
      },
    };
    new MicroModalHandler(modalId, callBacks);
  });

  formElement.addEventListener("submit", (event) => {
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
    // console.log(formInputs);
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
