"use strict";
import { CURRENTUSER } from "../../../utils/constants.js";
import {
  sendRequest,
  fetchUrlPathByName,
  formInputSerializer,
  setFormInputValues,
} from "../../../utils/helpers.js";
import { MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  // notes:api:manager:create, notes:api:manager:update, notes:api:manager:retrieve, notes:api:manager:delete
  const noteModalId = "note-form-modal";
  const noteModalElement = document.querySelector(`#${noteModalId}`);
  const notOwnerTagElement = noteModalElement.querySelector(".not-owner-tag");
  const noteModalFormElement = noteModalElement.querySelector("form");
  const noteModalTitleElement = noteModalElement.querySelector(".modal__title");
  const noteModalSubmitElement = noteModalElement.querySelector(
    "button[type='submit']"
  );
  const noteModalFormFieldsetElement =
    noteModalFormElement.querySelector("fieldset");
  const managerAddNoteBtn = document.querySelector("button#addNoteBtn");
  const managerViewNoteBtn = document.querySelectorAll(".managerViewNoteBtn");
  const managerDeleteNoteBtn = document.querySelectorAll(
    ".managerDeleteNoteBtn"
  );

  // create note button
  managerAddNoteBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: async () => {
        noteModalTitleElement.textContent = "Create Note";
        noteModalSubmitElement.textContent = "Create";
        noteModalFormElement["_method"].value = "POST";
        noteModalFormElement.setAttribute("method", "POST");
        const createUrl = await fetchUrlPathByName("notes:api:manager:create");
        noteModalFormElement.setAttribute("action", createUrl["urlPath"]);
      },
      onCloseCallback: () => {},
    };
    new MicroModalHandler(noteModalId, callBacks);
  });

  // add notes form submit form
  noteModalFormElement.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    noteModalFormFieldsetElement.disabled = true;
    const formData = formInputSerializer({
      formElement: currentTarget,
      excludedFields: ["_method"],
      isOrdered: true,
    });
    // console.log(formData);
    // throw new Error("dd");
    // const formData = {
    //   title: currentTarget["title"].value,
    //   body: currentTarget["body"].value,
    //   user: currentTarget["user"].value,
    //   note_section: currentTarget["note_section"].value,
    //   client: currentTarget["client"].value,
    //   created_by: currentTarget["user"].value,
    // };
    const requestOptions = {
      method: currentTarget["_method"].value,
      dataToSend: formData,
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
      });
  });

  // view note item event
  managerViewNoteBtn.forEach((btn) => {
    btn.addEventListener("click", async (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const noteId = data["noteId"];
      const retrieveUrl = await fetchUrlPathByName(
        "notes:api:manager:retrieve"
      );
      const updateUrl = await fetchUrlPathByName("notes:api:manager:update");
      const requestOptions = {
        method: "POST",
        dataToSend: { noteId: noteId },
        url: retrieveUrl["urlPath"],
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          const noteData = data["note"];
          const callBacks = {
            onOpenCallBack: () => {
              setFormInputValues(noteModalFormElement, noteData);
              noteModalTitleElement.textContent = "Update note";
              noteModalSubmitElement.textContent = "Update";
              noteModalFormElement.setAttribute("method", "PUT");
              noteModalFormElement.setAttribute("action", updateUrl["urlPath"]);
              noteModalFormElement["_method"].value = "PUT";
              if (noteData["created_by"] != CURRENTUSER) {
                notOwnerTagElement.classList.remove("is-hidden");
              } else {
                notOwnerTagElement.classList.add("is-hidden");
              }
              // retrieveNoteForm.elements["note_id"].value = noteData["id"];
              // retrieveNoteForm.elements["title"].value = noteData["title"];
              // retrieveNoteForm.elements["body"].value = noteData["body"];
              // retrieveNoteForm.elements["client"].value = noteData["client"];
              // retrieveNoteForm.elements["note_section"].value = noteData["note_section"];
            },
            onCloseCallback: () => {
              noteModalFormElement.reset();
            },
          };
          new MicroModalHandler(noteModalId, callBacks);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(
            `${JSON.stringify(error["user_error_msg"])}`,
            "danger"
          );
        });
    });
  });
  // delete note item
  managerDeleteNoteBtn.forEach((btn) => {
    btn.addEventListener("click", async (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const noteId = data["noteId"];
      const noteTitle = data["noteTitle"];
      const deleteUrl = await fetchUrlPathByName("notes:api:manager:delete");
      const confirmMsg = confirm(
        `Do you want to delete the note ${noteTitle}?`
      );
      if (confirmMsg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { noteId: noteId },
          url: deleteUrl["urlPath"],
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
});
