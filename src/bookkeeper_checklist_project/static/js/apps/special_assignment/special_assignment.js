"use strict";
import { getCookie } from "../../utils/cookie.js";
import {
  fetchUrlPathByName,
  formInputSerializer,
  sendRequest,
  UploadFileRequest,
} from "../../utils/helpers.js";
import { MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const modalId = "special-assignment-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const formElement = modalElement.querySelector("form");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const addSpecialAssignmentBtn = document.querySelector(
    "button#addSpecialAssignmentBtn"
  );

  addSpecialAssignmentBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: async () => {
        modalTitleElement.textContent = "Create new special assignmentBtn";
        submitButton.textContent = "Create";
        formElement.setAttribute("method", "POST");
        formElement["_method"].value = "POST";

        const createUrl = await fetchUrlPathByName(
          "special_assignment:api:special_assignment:create"
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
    const attachmentInput =
      currentTarget.querySelector("input[type='file']").files[0];
    // console.log(attachmentInput);
    const formInputs = formInputSerializer({
      formElement: currentTarget,
      excludedFields: ["_method", "attachment"],
      returnAsFormData: true,
    });
    // console.log(formInputs);
    const requestOptions = {
      method: currentTarget["_method"].value,
      dataToSend: formInputs,
      url: currentTarget.action,
    };
    // check if attachmentInput contains file
    if (attachmentInput) {
      formInputs.append("attachment", attachmentInput);
    }
    const uploadRequest = new UploadFileRequest(
      currentTarget.action,
      formInputs,
      getCookie("csrftoken"),
      currentTarget["_method"].value,
      false
    );
    const request = uploadRequest.sendRequest();
    request
      .then((data) => {
        console.log(data);
        showToastNotification(data, "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification("Error while add new document!", "danger");
      })
      .finally(() => {});
  });
});
