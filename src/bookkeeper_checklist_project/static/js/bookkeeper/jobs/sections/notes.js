"use strict";
import { showMicroModal, MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";
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
  CURRENTUSER,
} from "../../../utils/constants.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const noteModalID = "note-form-modal";
  const notesModalElement = document.querySelector(`#${noteModalID}`);
  const noteModalTitleElement =
    notesModalElement.querySelector(".modal__title");
  const noteModalSubmitBtn = notesModalElement.querySelector(
    "button[type='submit']"
  );
  const noteModalForm = notesModalElement.querySelector(`form`);
  // const noteElements = document.querySelectorAll(".noteElement");
  const updateNoteElementBtns = document.querySelectorAll(
    ".updateNoteElementBtn"
  );
  const bookkeeperDeleteNoteBtns = document.querySelectorAll(
    "button.bookkeeperDeleteNoteBtn"
  );
  const bookkeeperAddNoteToJobBtn = document.querySelector(
    "button#bookkeeperAddNoteToJobBtn"
  );

  // delete notes buttons events
  if (bookkeeperDeleteNoteBtns) {
    bookkeeperDeleteNoteBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const noteId = currentTarget.dataset["noteId"];
        const noteTitle = currentTarget.dataset["noteTitle"];
        const confirmMsg = confirm(`Do you want to delete note ${noteTitle}?`);
        if (confirmMsg) {
          const requestOptions = {
            method: "DELETE",
            dataToSend: { noteId: noteId },
            url: window.localStorage.getItem("BookkeeperNotesApiDeleteUrl"),
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
            });
        }
      });
    });
  }

  // update note button
  if (updateNoteElementBtns) {
    updateNoteElementBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const noteId = currentTarget.dataset["noteId"];
        const isOwner = Boolean(parseInt(currentTarget.dataset["owner"]));
        const callBacks = {
          onOpenCallBack: () => {
            // noteModalForm.action = window.localStorage.getItem(
            //   "BookkeeperNotesApiCreateUrl"
            // );
            noteModalSubmitBtn.textContent = "Update";
            noteModalForm.elements["_method"].value = "PUT";
            noteModalForm.setAttribute(
              "action",
              window.localStorage.getItem("BookkeeperNotesApiUpdateUrl")
            );
            noteModalTitleElement.textContent = "Update note";
            const retrieveUrl = window.localStorage.getItem(
              "BookkeeperNotesApiRetrieveUrl"
            );
            const requestOptions = {
              method: "POST",
              dataToSend: { noteId: noteId },
              url: retrieveUrl,
            };
            // console.log(requestOptions);
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const noteData = data["note"];
                setFormInputValues(noteModalForm, noteData);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(
                  `${JSON.stringify(error["user_error_msg"])}`,
                  "danger"
                );
              });
          },
          onCloseCallback: () => {
            noteModalSubmitBtn.disabled = false;
            noteModalForm.reset();
          },
        };
        const modalHandler = new MicroModalHandler(noteModalID, callBacks);
        if (isOwner === true) {
          noteModalSubmitBtn.hidden = false;
        } else {
          noteModalSubmitBtn.hidden = true;
        }
      });
    });
  }
  // add note button
  bookkeeperAddNoteToJobBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: () => {
        noteModalForm.action = window.localStorage.getItem(
          "BookkeeperNotesApiCreateUrl"
        );
        noteModalForm.method = "POST";
        noteModalForm.elements["_method"].value = "POST";
        noteModalTitleElement.textContent = "Create new note";
        noteModalSubmitBtn.textContent = "Create";
        noteModalSubmitBtn.hidden = false;
      },
      onCloseCallback: () => {
        noteModalSubmitBtn.disabled = false;
      },
    };
    const modalHandler = new MicroModalHandler(noteModalID, callBacks);
  });

  // note form
  if (noteModalForm) {
    noteModalForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      // check if the submit is for update not create
      if (currentTarget["_method"].value === "PUT") {
        if (currentTarget["created_by"].value !== CURRENTUSER) {
          return false;
        }
      }
      const fieldset = currentTarget.querySelector("fieldset");
      const formInputs = formInputSerializer({ formElement: currentTarget });
      fieldset.disabled = true;
      noteModalSubmitBtn.disabled = true;
      const requestOptions = {
        method: currentTarget.elements["_method"].value,
        dataToSend: formInputs,
        url: currentTarget.action,
      };
      // console.log(requestOptions);
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
        .finally(() => {
          fieldset.disabled = false;
          noteModalSubmitBtn.disabled = false;
          // noteModalForm.reset();
        });
    });
  }
});
