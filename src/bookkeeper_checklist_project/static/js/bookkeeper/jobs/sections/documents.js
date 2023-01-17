"use strict";
import { showMicroModal, MicroModalHandler } from "../../../utils/model-box.js";
import {
  enableInputsOnLoad,
  formInputSerializer,
  sendRequest,
  setFormInputValues,
  UploadFileRequest,
} from "../../../utils/helpers.js";
import { getCookie } from "../../../utils/cookie.js";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../../utils/constants.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const bookkeeperAddDocumentToJobBtn = document.querySelector(
    "button#bookkeeperAddDocumentToJobBtn"
  );
  const documentFormModalId = "document-form-modal";
  const documentTitleFormModalElement = document.querySelector(
    "#document-form-modal-title"
  );
  const documentForm = document
    .querySelector("#document-form-modal")
    .querySelector("form");
  const addSubmitButton = document.querySelector(
    `button[form='${documentForm.id}']`
  );
  const documentModalFooterElement = document.querySelector(
    "#document-modal-footer"
  );
  const documentElements = document.querySelectorAll("a.documentElement");

  const bookkeeperDeleteDocumentBtns = document.querySelectorAll(
    ".bookkeeperDeleteDocumentBtn"
  );
  // delete document buttons
  if (bookkeeperDeleteDocumentBtns) {
    bookkeeperDeleteDocumentBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const parent = currentTarget.parentElement.parentElement.parentElement;
        const confirmMsg = confirm("Do you want to delete the document?");
        if (confirmMsg) {
          const documentId = currentTarget.dataset["documentId"];
          const deleteUrl = window.localStorage.getItem(
            "BookkeeperDocumentsApiDeleteUrl"
          );
          const requestOptions = {
            method: "DELETE",
            dataToSend: { documentId: documentId },
            url: deleteUrl,
          };
          const request = sendRequest(requestOptions);
          request
            .then((data) => {
              showToastNotification(data["msg"], "success");
              parent.remove();
              //   setTimeout(() => {
              //     window.location.reload();
              //   }, 500);
            })
            .catch((error) => {
              console.error(error);
              showToastNotification(
                `${JSON.stringify(error["user_error_msg"])}`,
                "danger"
              );
            });
        }
      });
    });
  }
  // open update document modal links
  if (documentElements) {
    documentElements.forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const retrieveUrl = window.localStorage.getItem(
          "BookkeeperDocumentsApiRetrieveUrl"
        );
        const documentID = currentTarget.dataset["documentId"];
        const docOwner = Boolean(parseInt(currentTarget.dataset["owner"]));
        const callBacks = {
          onOpenCallBack: () => {
            documentTitleFormModalElement.textContent = "Update document";
            addSubmitButton.hidden = true;
            // console.log(documentForm.method);
            // documentForm.setAttribute("method", "PUT");
            const requestOptions = {
              method: "POST",
              dataToSend: { documentId: documentID },
              url: retrieveUrl,
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const documentData = data["document"];
                documentData["document_file_id"] =
                  documentData["document_file"];
                const fieldset = documentForm.querySelector("fieldset");
                const idInput = document.createElement("input");
                idInput.type = "hidden";
                idInput.id = "id";
                idInput.name = "id";
                // idInput.value = documentData["id"];
                fieldset.appendChild(idInput);
                setFormInputValues(documentForm, documentData);
                // create document download link or button
                const downloadBtn = document.createElement("a");
                downloadBtn.href = documentData["document_file"];
                downloadBtn.download = documentData["document_file"];
                downloadBtn.id = "tmpDownloadFileLink";
                downloadBtn.innerHTML = `<i class="fa-solid fa-2x fa-download"></i>`;
                downloadBtn.title = "Download document file";
                downloadBtn.target = "_blank";
                fieldset.appendChild(downloadBtn);
                // console.log(documentData);
                // check if the document created by current logged in bookkeeper
                // if (docOwner === true) {
                //   addSubmitButton.hidden = false;
                // } else {
                //   addSubmitButton.hidden = true;
                // }
                // set the form action to update url
                documentForm.action = window.localStorage.getItem(
                  "BookkeeperApiUpdateUrl"
                );
                documentForm.method = "PUT";
                // new MicroModalHandler("update-document-form-modal", {});
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(
                  `${JSON.stringify(error["user_error_msg"])}`,
                  "danger"
                );
              })
              .finally(() => {
                console.warn("Finally");
              });
          },
          onCloseCallback: () => {
            documentTitleFormModalElement.textContent = "";
            addSubmitButton.hidden = true;
            documentForm.reset();
            document.querySelector("a#tmpDownloadFileLink").remove();
          },
        };
        const modalHandler = new MicroModalHandler(
          documentFormModalId,
          callBacks
        );

        addSubmitButton.textContent = "Update";
      });
    });
  }

  // add document button, which will handle form submit creation
  bookkeeperAddDocumentToJobBtn.addEventListener("click", (event) => {
    // @follow-up
    const callBacks = {
      onOpenCallBack: () => {
        addSubmitButton.hidden = false;
        documentTitleFormModalElement.textContent = "Add new document";
        documentForm.method = "POST";
        documentForm.action = window.localStorage.getItem(
          "BookkeeperDocumentsApiCreateUrl"
        );
      },
      onCloseCallback: () => {
        documentTitleFormModalElement.textContent = "";
        documentForm.method = "";
        documentForm.action = "";
      },
    };
    const modalHandler = new MicroModalHandler(documentFormModalId, callBacks);

    addSubmitButton.textContent = "Create";
  });

  // add new document form submit event
  documentForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const formInputs = formInputSerializer(currentTarget);
    delete formInputs["document_file"];
    const formData = new FormData();
    const fieldset = documentForm.querySelector("fieldset");
    const documentFile = currentTarget["id_document_file"].files[0];
    fieldset.disabled = true;
    for (const formKey in formInputs) {
      if (Object.hasOwnProperty.call(formInputs, formKey)) {
        const element = formInputs[formKey];
        formData.append(formKey, element);
      }
    }
    formData.append("document_file", documentFile);
    console.log(currentTarget.method);
    const uploadRequest = new UploadFileRequest(
      currentTarget.action,
      formData,
      getCookie("csrftoken"),
      currentTarget.method,
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
      .finally(() => {
        fieldset.disabled = false;
      });
  });
});
