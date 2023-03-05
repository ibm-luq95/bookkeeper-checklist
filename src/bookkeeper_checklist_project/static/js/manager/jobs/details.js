"use strict";

import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import {
  enableInputsOnLoad,
  formInputSerializer,
  sendRequest,
  UploadFileRequest,
} from "../../utils/helpers.js";
import { getCookie } from "../../utils/cookie.js";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
  CURRENTUSER,
} from "../../utils/constants.js";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const managerAddTaskBtn = document.querySelector("button#managerAddTaskBtn");
  const taskViewBtn = document.querySelectorAll(".taskViewBtn");
  const taskDeleteBtn = document.querySelectorAll("button.taskDeleteBtn");
  const managerAddNoteToJobBtn = document.querySelector("button#managerAddNoteToJobBtn");
  const managerAddDocumentToJobBtn = document.querySelector("button#managerAddDocumentToJobBtn");
  const managerAddNewTaskForm = document.querySelector("form#managerAddNewTaskForm");
  const noteElements = document.querySelectorAll("a.noteElement");
  const documentElements = document.querySelectorAll("a.documentElement");
  const managerUpdateTaskForm = document.querySelector("form#managerUpdateTaskForm");
  const managerTaskCheckboxInputs = document.querySelectorAll("input.managerTaskCheckboxInput");
  const managerDeleteDocumentBtns = document.querySelectorAll(".managerDeleteDocumentBtn");
  const managerDeleteNotesBtns = document.querySelectorAll(".managerDeleteNotesBtns");
  const allCheckedTasks = new Array();
  const managerTaskParentCheckboxInput = document.querySelector(
    "input#managerTaskParentCheckboxInput",
  );
/*   const clientsTable = $("#managerJobTasksTable").DataTable({
    autoWidth: true,
    processing: true,
    info: false,
    // "paging": false,
    // stateSave: true,
    stateSaveCallback: function (settings, data) {
      localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
    },
    stateLoadCallback: function (settings) {
      return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
    },
    fixedHeader: true,
    responsive: true,
    dom: "Bfrtip",
    // buttons: ["Update", "csv", "pdf"],
    buttons: [
      {
        text: "Done",
        action: (e, dt, node, config) => {
          // @audit
          if (allCheckedTasks.length <= 0) {
            alert("No tasks checked");
          } else {
            console.log(allCheckedTasks);
          }
        },
      },
      "csv",
      "pdf",
    ],
  }); */

  /* managerAddTaskBtn.addEventListener("click", (ev) => {
    showMicroModal("tasks-form-modal");
  }); */

  // delete task buttons from tasks table
  managerDeleteNotesBtns.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const noteId = currentTarget.dataset["noteId"];
      const noteTitle = currentTarget.dataset["noteTitle"];
      const msg = confirm(`Do you want to delete note ${noteTitle}?`);
      const url = window.localStorage.getItem("DeleteNoteUrl");
      if (msg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { noteId: noteId },
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification("Note deleted", "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      }
    });
  });

  // delete document button
  managerDeleteDocumentBtns.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const documentId = currentTarget.dataset["documentId"];
      const documentTitle = currentTarget.dataset["documentTitle"];
      const msg = confirm(`Do you want to delete ${documentTitle}?`);
      const url = window.localStorage.getItem("DeleteDocumentUrl");
      if (msg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { documentId: documentId },
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification("Document deleted successfully", "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      }
    });
  });

  if (managerTaskParentCheckboxInput) {
    managerTaskParentCheckboxInput.addEventListener("change", (ev) => {
      const checked = ev.currentTarget.checked;
      if (checked === true) {
        managerTaskCheckboxInputs.forEach((input) => {
          input.checked = true;
        });
      } else {
        managerTaskCheckboxInputs.forEach((input) => {
          input.checked = false;
        });
      }
      const changeEvent = new Event("change");
      managerTaskCheckboxInputs.forEach((input) => {
        input.dispatchEvent(changeEvent);
      });
    });
  }

  managerTaskCheckboxInputs.forEach((input) => {
    input.addEventListener("change", (event) => {
      const currentTarget = event.currentTarget;
      const taskId = currentTarget.value;
      if (event.currentTarget.checked === true) {
        allCheckedTasks.push(taskId);
      } else {
        const idx = allCheckedTasks.indexOf(taskId);
        // delete allCheckedTasks[idx];
        allCheckedTasks.splice(idx);
      }
      // console.log(allCheckedTasks);
    });
  });

  // show note elements
  if (noteElements) {
    const managerUpdateNoteForm = document.querySelector("form#managerUpdateNoteForm");
    noteElements.forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const dataset = currentTarget.dataset;
        const noteId = dataset["noteId"];
        const url = window.localStorage.getItem("retrieveNoteUrl");
        //update-note-form-modal
        const requestOptions = {
          method: "POST",
          dataToSend: { noteId: noteId },
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            const noteData = data["note"];
            // console.log(noteData);
            const callBacks = {
              onOpenCallBack: () => {
                managerUpdateNoteForm.elements["id"].value = noteData["id"];
                managerUpdateNoteForm.elements["title"].value = noteData["title"];
                managerUpdateNoteForm.elements["body"].value = noteData["body"];
                managerUpdateNoteForm.elements["client"].value = noteData["client"];
                managerUpdateNoteForm.elements["note_section"].value = noteData["note_section"];
              },
              onCloseCallback: () => {
                managerUpdateNoteForm.elements["title"].value = "";
                managerUpdateNoteForm.elements["id"].value = "";
                managerUpdateNoteForm.elements["body"].value = "";
                managerUpdateNoteForm.elements["client"].value = "";
                managerUpdateNoteForm.elements["note_section"].value = "";
              },
            };
            const modlaHandler = new MicroModalHandler("update-note-form-modal", callBacks);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      });
    });

    /* managerUpdateNoteForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fullUrl = event.currentTarget.action;
      const formData = formInputSerializer({formElement: currentTarget});
      const requestOptions = {
        method: "PUT",
        dataToSend: formData,
        url: fullUrl,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification("Note updated", "success");
          setTimeout(() => {
            window.location.reload();
          }, 500);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        })
        .finally(() => {
          console.warn("Finally");
        });
    }); */
  }

  // show document elements
    if (documentElements) {
    documentElements.forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const dataset = currentTarget.dataset;
        const documentId = dataset["documentId"];
        const url = window.localStorage.getItem("RetrieveDocumentUrl");
        const requestOptions = {
          method: "POST",
          dataToSend: { documentId: documentId },
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            new MicroModalHandler("document-form-modal", {});
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            console.warn("Finally");
          });
      });
    });
  }
  // add new task form
  /* managerAddNewTaskForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const fieldset = currentTarget.querySelector("fieldset");
    fieldset.disabled = true;
    const formData = formInputSerializer({formElement: currentTarget});
    Array.from(currentTarget.elements).forEach((element) => {
      element.classList.remove("is-danger");
    });
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification("Task created successfully", "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        fieldset.disabled = false;
        const userErrors = error["user_error_msg"];
        for (const key in userErrors) {
          if (Object.hasOwnProperty.call(userErrors, key)) {
            const element = userErrors[key];
            currentTarget[key].classList.add(...["is-danger"]);
          }
        }
      });
  }); */

  /* managerUpdateTaskForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const formData = formInputSerializer({formElement: currentTarget});
    const url = currentTarget.action;
    const fieldset = currentTarget.querySelector("fieldset");
    fieldset.disabled = true;
    const requestOptions = {
      method: "PUT",
      dataToSend: formData,
      url: url,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        console.log(data);
        showToastNotification(`${JSON.stringify(data["msg"])}`, "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        const userErrors = error["user_error_msg"];
        for (const key in userErrors) {
          if (Object.hasOwnProperty.call(userErrors, key)) {
            const element = userErrors[key];
            currentTarget[key].classList.add(...["is-danger"]);
          }
        }
      })
      .finally(() => {
        fieldset.disabled = false;
      });
  }); */

  taskViewBtn.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
      ev.preventDefault();
      const currentTarget = ev.currentTarget;
      const taskId = currentTarget.dataset["taskId"];
      const url = window.localStorage.getItem("RetrieveTaskUrl");
      //update-tasks-form-modal
      const callBacks = {
        onOpenCallBack: () => {
          const requestOptions = {
            method: "POST",
            dataToSend: { taskId: taskId },
            url: url,
          };
          const request = sendRequest(requestOptions);
          request
            .then((data) => {
              const taskObject = data["task"];
              // console.log(taskObject);
              managerUpdateTaskForm["job"].value = taskObject["job"];
              managerUpdateTaskForm["taskId"].value = taskObject["id"];
              managerUpdateTaskForm["title"].value = taskObject["title"];
              managerUpdateTaskForm["task_type"].value = taskObject["task_type"];
              managerUpdateTaskForm["status"].value = taskObject["status"];
              managerUpdateTaskForm["hints"].value = taskObject["hints"];
              managerUpdateTaskForm["additional_notes"].value = taskObject["additional_notes"];
              managerUpdateTaskForm["start_date"].value = taskObject["start_date"];
              managerUpdateTaskForm["due_date"].value = taskObject["due_date"];
             /*  if (taskObject["is_completed"] === true) {
                managerUpdateTaskForm["is_completed"].checked = true;
              } else {
                managerUpdateTaskForm["is_completed"].checked = false;
              } */
            })
            .catch((error) => {
              console.error(error);
              showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
            })
            .finally(() => {
              // jobsFormFieldset.disabled = false;
              // managerJobsLoaderBtn.hidden = true;
            });
        },
        onCloseCallback: () => {},
      };
      const modlaHandler = new MicroModalHandler("update-tasks-form-modal", callBacks);
    });
  });
  taskDeleteBtn.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
      const currentTarget = ev.currentTarget;
      const taskId = currentTarget.dataset["taskId"];
      const taskTitle = currentTarget.dataset["taskTitle"];
      const msg = confirm(`Do you want delete task ${taskTitle}?`);
      const url = window.localStorage.getItem("DeleteTaskUrl");
      if (msg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { taskId: taskId },
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            showToastNotification(`${JSON.stringify(data["msg"])}`, "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {});
      }
    });
  });

  // add note button event
  /* managerAddNoteToJobBtn.addEventListener("click", (event) => {
    // @follow-up
    const callBacks = {
      onOpenCallBack: () => {},
      onCloseCallback: () => {},
    };
    const modlaHandler = new MicroModalHandler("note-form-modal", callBacks);
    const managerAddNewNoteForm = document.querySelector("form#managerAddNewNoteForm");
    const fieldset = managerAddNewNoteForm.querySelector("fieldset");

    managerAddNewNoteForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const formElements = formInputSerializer({formElement: currentTarget});
      fieldset.disabled = true;
      // console.log(formElements);
      // throw new Error("s");
      const requestOptions = {
        method: "POST",
        dataToSend: formElements,
        url: currentTarget.action,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification("Note created successfully", "success");
          setTimeout(() => {
            window.location.reload();
          }, 500);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  }); */

  // add document button event
  /* managerAddDocumentToJobBtn.addEventListener("click", (event) => {
    // @follow-up
    const callBacks = {
      onOpenCallBack: () => {},
      onCloseCallback: () => {},
    };
    const modlaHandler = new MicroModalHandler("document-form-modal", callBacks);
    const managerAddNewDocumentForm = document.querySelector("form#managerAddNewDocumentForm");
    const fieldset = managerAddNewDocumentForm.querySelector("fieldset");

    managerAddNewDocumentForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const documentFile = currentTarget["id_document_file"].files[0];
      fieldset.disabled = true;
      const formData = new FormData();
      // console.log(currentTarget.action);
      // console.log(currentTarget.elements);
      formData.append("title", currentTarget["id_title"].value);
      formData.append("document_section", currentTarget["id_document_section"].value);
      formData.append("client", currentTarget["client"].value);
      formData.append("user", currentTarget["user"].value);
      formData.append("job", currentTarget["job"].value);
      formData.append("document_file", documentFile);
      const requestOptions = {
        method: "POST",
        dataToSend: formData,
        url: currentTarget.action,
      };
      const uploadRequest = new UploadFileRequest(
        currentTarget.action,
        formData,
        getCookie("csrftoken"),
        "POST",
        false,
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
  }); */
});
