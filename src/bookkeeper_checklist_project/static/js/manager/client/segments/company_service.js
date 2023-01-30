"use strict";
import {
  eyeIconHTMLCode,
  eyeSlashIconHTMLCode,
} from "../../../utils/constants.js";
import {
  sendRequest,
  fetchUrlPathByName,
  formInputSerializer,
  setFormInputValues,
  addTxtToClipboardWithNotification,
} from "../../../utils/helpers.js";
import { MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  //company-services:api:manager:create
  const modalId = "company-services-form-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const companyServiceForm = modalElement.querySelector("form");
  const fieldset = companyServiceForm.querySelector("fieldset");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const copyASurlBtns = document.querySelectorAll(".copyASurlBtn");
  const copyASUsernameBtns = document.querySelectorAll(".copyASUsernameBtn");
  const copyASUPasswordBtns = document.querySelectorAll(".copyASUPasswordBtn");
  const managerViewASBtns = document.querySelectorAll(".managerViewASBtn");
  const managerDeleteASBtns = document.querySelectorAll(".managerDeleteASBtn");
  const managerAddCompanyServiceBtn = document.querySelector(
    "button#managerAddCompanyServiceBtn"
  );
  const managerCompanyServicesLoaderBtn = document.querySelector(
    "button#managerCompanyServicesLoaderBtn"
  );
  const allShowASPasswordBtns = document.querySelectorAll(
    ".showASUPasswordBtn"
  );

  // view company & service to update
  if (managerViewASBtns) {
    managerViewASBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const serviceId = currentTarget.dataset["serviceId"];
        alert(serviceId)
      });
    });
  }

  // copy company & services url
  if (copyASurlBtns) {
    copyASurlBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const url = currentTarget.dataset["urlValue"];
        addTxtToClipboardWithNotification({ textWillCopy: url, label: "url" });
      });
    });
  }

  // copy company & services password
  if (copyASUPasswordBtns) {
    copyASUPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const password = currentTarget.dataset["passwordValue"];
        addTxtToClipboardWithNotification({
          textWillCopy: password,
          label: "password",
        });
      });
    });
  }

  // copy company & services username
  if (copyASUsernameBtns) {
    copyASUsernameBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const username = currentTarget.dataset["usernameValue"];
        addTxtToClipboardWithNotification({
          textWillCopy: username,
          label: "username",
        });
      });
    });
  }
  // show company and services passwords
  if (allShowASPasswordBtns) {
    allShowASPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const visibilityStatus = Boolean(
          parseInt(currentTarget.dataset["visibilityStatus"])
        );
        const passwordInputId = currentTarget.dataset["passwordInput"];
        const passwordInputElement = document.querySelector(
          `#${passwordInputId}`
        );
        if (visibilityStatus === true) {
          currentTarget.innerHTML = eyeIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 0;
          passwordInputElement.type = "password";
        } else {
          currentTarget.innerHTML = eyeSlashIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 1;
          passwordInputElement.type = "text";
        }
      });
    });
  }
  // create new service button
  managerAddCompanyServiceBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: async () => {
        modalTitleElement.textContent = "Create";
        submitButton.textContent = "Create";
        companyServiceForm.setAttribute("method", "POST");
        companyServiceForm["_method"].value = "POST";

        const createUrl = await fetchUrlPathByName(
          "company-services:api:manager:create"
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
    console.log(formInputs);
    /* const formData = {
      service_name: currentTarget["service_name"].value,
      label: currentTarget["label"].value,
      username: currentTarget["username"].value,
      password: currentTarget["password"].value,
      client: currentTarget["client"].value,
      user: currentTarget["user"].value,
      url: currentTarget["url"].value,
      created_by: currentTarget["user"].value,
    }; */
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
