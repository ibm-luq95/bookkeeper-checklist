"use strict";
import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import { enableInputsOnLoad, sendRequest, UploadFileRequest } from "../../utils/helpers.js";
import { getCookie } from "../../utils/cookie.js";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";
document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const managerShowClientImportantContactBtn = document.querySelector(
    "button#managerShowClientImportantContactBtn",
  );
  const addDocumentFormWrapper = document.querySelector("div#addDocumentFormWrapper");
  const addDocumentForm = addDocumentFormWrapper.querySelector("form#addDocumentForm");
  const addDocumentFormFieldSet = addDocumentForm.querySelector("fieldset");
  const managerAddJobBtn = document.querySelector("button#managerAddJobBtn");
  const managerDocumentLoaderBtn = document.querySelector("button#managerDocumentLoaderBtn");
  const addNoteFormWrapper = document.querySelector("div#addNoteFormWrapper");
  const addNoteForm = addNoteFormWrapper.querySelector("form#addNoteForm");
  const managerAddDocumentBtn = document.querySelector("button#managerAddDocumentBtn");
  const managerAddNoteBtn = document.querySelector("button#managerAddNoteBtn");
  const managerViewNoteBtn = document.querySelectorAll("button.managerViewNoteBtn");
  const managerDeleteNoteBtn = document.querySelectorAll("button.managerDeleteNoteBtn");
  const retrieveNoteFormWrapper = document.querySelector("div#retrieveNoteFormWrapper");
  const retrieveNoteForm = retrieveNoteFormWrapper.querySelector("form#retrieveNoteForm");
  const retrieveNoteFieldset = retrieveNoteFormWrapper.querySelector("fieldset");
  const companyServicesFormWrapper = document.querySelector("div#companyServicesFormWrapper");
  const companyServiceForm = companyServicesFormWrapper.querySelector("form#companyServiceForm");
  const companyServiceFieldset = companyServicesFormWrapper.querySelector("fieldset");
  const managerAddCompanyServiceBtn = document.querySelector("button#managerAddCompanyServiceBtn");
  const managerCompanyServicesLoaderBtn = document.querySelector(
    "button#managerCompanyServicesLoaderBtn",
  );
  const managerDeleteDocumentBtn = document.querySelectorAll(".managerDeleteDocumentBtn");

  const jobsFormWrapper = document.querySelector("div#jobsFormWrapper");
  const managerJobsLoaderBtn = document.querySelector("button#managerJobsLoaderBtn");
  const jobsForm = jobsFormWrapper.querySelector("form#jobsForm");
  const jobsFormFieldset = jobsForm.querySelector("fieldset");

  const managerAddTasksBtn = document.querySelector("button#managerAddTasksBtn");
  const tasksCreateFormWrapper = document.querySelector("div#tasksCreateFormWrapper");
  const tasksCreateForm = tasksCreateFormWrapper.querySelector("form#tasksCreateForm");
  const tasksCreateFormFieldSet = tasksCreateForm.querySelector("fieldset");
  const managerTasksLoaderBtn = document.querySelector("button#managerTasksLoaderBtn");
  const managerDeleteJobBtn = document.querySelectorAll("button.managerDeleteJobBtn");
  const managerViewJobBtn = document.querySelectorAll("button.managerViewJobBtn");
  const managerViewTaskBtn = document.querySelectorAll("button.managerViewTaskBtn");
  const managerDeleteTaskBtn = document.querySelectorAll("button.managerDeleteTaskBtn");

  if (managerAddDocumentBtn) {
    managerAddDocumentBtn.addEventListener("click", (e) => {
      e.preventDefault();
      showMicroModal("document-form-modal");
    });
  }
  managerAddJobBtn.addEventListener("click", (event) => {
    showMicroModal("jobs-create-form-modal");
  });
  managerAddTasksBtn.addEventListener("click", (event) => {
    showMicroModal("tasks-create-form-modal");
  });
  managerAddCompanyServiceBtn.addEventListener("click", (event) => {
    showMicroModal("company-services-form-modal");
  });
  managerShowClientImportantContactBtn.addEventListener("click", (ev) => {
    showMicroModal("important-contact-form-modal");
  });
  managerAddNoteBtn.addEventListener("click", (event) => {
    showMicroModal("notes-form-modal");
  });

  // add document form event
  addDocumentForm.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const currentTarget = addDocumentForm;
    const documentFile = currentTarget["id_document_file"].files[0];
    addDocumentFormFieldSet.disabled = true;
    managerDocumentLoaderBtn.hidden = false;
    const formData = new FormData();
    // console.log(currentTarget.action);
    // console.log(currentTarget.elements);
    formData.append("title", currentTarget["id_title"].value);
    formData.append("document_section", currentTarget["id_document_section"].value);
    formData.append("client", currentTarget.querySelector("#client").value);
    formData.append("user", currentTarget.querySelector("#user").value);
    formData.append("document_file", documentFile);
    /* formData.forEach((formDataItem) => {
      console.log(formDataItem);
    }); */
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
      // contentType: "multipart/form-data",
    };
    const uploadRequest = new UploadFileRequest(
      addDocumentForm.action,
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
        }, 1000);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification("Error while add new document!", "danger");
      })
      .finally(() => {
        addDocumentFormFieldSet.disabled = false;
        managerDocumentLoaderBtn.hidden = true;
      });
  });

  // add notes form submit form
  addNoteForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = addNoteForm;
    retrieveNoteFieldset.disabled = true;
    /* for (const input of currentTarget.elements) {
      console.log(input);
    } */
    const formData = {
      title: currentTarget["title"].value,
      body: currentTarget["body"].value,
      user: currentTarget["user"].value,
      note_section: currentTarget["note_section"].value,
      client: currentTarget["client"].value,
    };
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
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
      });
  });

  // view note item event
  managerViewNoteBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const noteId = data["noteId"];
      const url = window.localStorage.getItem("retrieveNoteUrl");
      const managerNoteLoaderBtn = document.querySelector("button#managerNoteLoaderBtn");
      // const fullUrl = window.localStorage.getItem("origin") + url;
      const fullUrl = window.location.origin + url;
      const requestOptions = {
        method: "POST",
        dataToSend: { noteId: noteId },
        url: fullUrl,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          const noteData = data["note"];
          managerNoteLoaderBtn.hidden = true;
          const callBacks = {
            onOpenCallBack: () => {
              retrieveNoteForm.elements["note_id"].value = noteData["id"];
              retrieveNoteForm.elements["title"].value = noteData["title"];
              retrieveNoteForm.elements["body"].value = noteData["body"];
              retrieveNoteForm.elements["client"].value = noteData["client"];
              retrieveNoteForm.elements["note_section"].value = noteData["note_section"];
            },
            onCloseCallback: () => {
              retrieveNoteForm.elements["title"].value = "";
              retrieveNoteForm.elements["body"].value = "";
              retrieveNoteForm.elements["client"].value = "";
              retrieveNoteForm.elements["note_section"].value = "";
            },
          };
          const modlaHandler = new MicroModalHandler("note-retrieve-modal", callBacks);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        });
    });
  });
  // delete note item
  managerDeleteNoteBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const fullUrl = window.location.origin + window.localStorage.getItem("DeleteNoteUrl");
      const noteId = data["noteId"];
      const confirmMsg = confirm("Do you want to delete the note?");
      if (confirmMsg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { noteId: noteId },
          url: fullUrl,
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

  // update note event
  retrieveNoteForm.addEventListener("submit", (event) => {
    event.preventDefault();
    //const fullUrl = window.location.origin + window.localStorage.getItem("UpdateNoteUrl");
    const fullUrl = event.currentTarget.action;
    managerNoteLoaderBtn.hidden = false;
    retrieveNoteFieldset.disabled = true;
    const updatedData = {
      id: retrieveNoteForm.elements["note_id"].value,
      title: retrieveNoteForm.elements["title"].value,
      body: retrieveNoteForm.elements["body"].value,
      note_section: retrieveNoteForm.elements["note_section"].value,
      client: retrieveNoteForm.elements["client"].value,
      user: retrieveNoteForm.elements["user"].value,
    };
    const requestOptions = {
      method: "PUT",
      dataToSend: updatedData,
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
        managerNoteLoaderBtn.hidden = true;
        retrieveNoteFieldset.disabled = false;
        console.warn("Finally");
      });
  });
  const clipboardJs = new ClipboardJS(".copyBtn");
  clipboardJs.on("success", (e) => {
    // console.info("Action:", e.action);
    // console.info("Text:", e.text);
    // console.info("Trigger:", e.trigger);
    e.clearSelection();
    const copiedText = e.text;
    const element = e.trigger;
    const textType = element.dataset["textType"];
    switch (textType) {
      case "username":
        showToastNotification(`Username ${copiedText} copied successfully`, "success");
        break;

      case "password":
        showToastNotification(`Password copied successfully`, "success");
        break;
      case "url":
        showToastNotification(`Url copied successfully`, "success");
        break;
    }
  });
  // add new company service form event
  companyServiceForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    companyServiceFieldset.disabled = true;
    managerCompanyServicesLoaderBtn.hidden = false;
    const formData = {
      service_name: currentTarget["service_name"].value,
      label: currentTarget["label"].value,
      email: currentTarget["email"].value,
      password: currentTarget["password"].value,
      client: currentTarget["client"].value,
      user: currentTarget["user"].value,
      url: currentTarget["url"].value,
    };
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification("Service created successfully", "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
      })
      .finally(() => {
        companyServiceFieldset.disabled = false;
        managerCompanyServicesLoaderBtn.hidden = true;
      });
  });

  const allShowASPasswordBtns = document.querySelectorAll(".showASUPasswordBtn");
  allShowASPasswordBtns.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const visibilityStatus = Boolean(parseInt(currentTarget.dataset["visibilityStatus"]));
      const passwordInputId = currentTarget.dataset["passwordInput"];
      const passwordInputElement = document.querySelector(`#${passwordInputId}`);
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

  // delete document buttons
  managerDeleteDocumentBtn.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
      const DeleteDocumentUrl = window.localStorage.getItem("DeleteDocumentUrl");
      const fullUrl = window.location.origin + DeleteDocumentUrl;
      const currentTarget = ev.currentTarget;
      const documentId = currentTarget.dataset["documentId"];
      const documentTitle = currentTarget.dataset["documentTitle"];
      const msg = confirm(`Do you want to delete document ${documentTitle}?`);
      if (msg === true) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { documentId: documentId },
          url: fullUrl,
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

  // create new job form event
  jobsForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    jobsFormFieldset.disabled = true;
    managerJobsLoaderBtn.hidden = false;
    const bookkeepersArray = new Array();
    const tasksArray = new Array();
    console.log(currentTarget["tasks"]);
    console.log(currentTarget["bookkeeper"]);
    console.log(currentTarget["bookkeeper"].length);
    // check if bookkeeper exists
    try {
      if (currentTarget["bookkeeper"]) {
        currentTarget["bookkeeper"].forEach((input) => {
          if (input.checked === true) {
            bookkeepersArray.push(input.value);
          }
        });
      }
    } catch (er) {
      if (er instanceof TypeError) {
        // in case the bookkeeper is single one not multiple
        bookkeepersArray.push(currentTarget["bookkeeper"].value);
      }
    }

    // check if tasks exists
    if (currentTarget["tasks"]) {
      currentTarget["tasks"].forEach((input) => {
        if (input.checked === true) {
          tasksArray.push(input.value);
        }
      });
    }

    // throw new Error("s");
    const formData = {
      bookkeeper: bookkeepersArray,
      title: currentTarget["title"].value,
      description: currentTarget["description"].value,
      due_date: currentTarget["due_date"].value,
      client: currentTarget["client"].value,
      status: currentTarget["status"].value,
      note: currentTarget["note"].value,
      job_type: currentTarget["job_type"].value,
      tasks: tasksArray,
    };
    console.log(formData);
    const requestOptions = {
      method: "POST",
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
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
      })
      .finally(() => {
        jobsFormFieldset.disabled = false;
        managerJobsLoaderBtn.hidden = true;
      });
  });

  // create new task form event
  tasksCreateForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const submitBtn = document.querySelector("button#managerTasksCreateSubmitBtn");
    const currentTarget = event.currentTarget;
    tasksCreateFormFieldSet.disabled = true;
    managerTasksLoaderBtn.hidden = false;
    submitBtn.disabled = true;
    submitBtn.classList.add("is-disabled");

    const formData = {
      title: currentTarget["title"].value,
      task_type: currentTarget["task_type"].value,
      is_completed: currentTarget["is_completed"].checked,
      hints: currentTarget["hints"].value,
      user: currentTarget["user"].value,
      additional_notes: currentTarget["additional_notes"].value,
      // client: currentTarget["client"].value,
      job: currentTarget["job"].value,
      due_date: currentTarget["due_date"].value,
      start_date: currentTarget["start_date"].value,
    };
    console.log(formData);
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
      });
  });

  // delete job buttons
  managerDeleteJobBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const deleteJobUrl = window.localStorage.getItem("DeleteJobUrl");
      const jobId = event.currentTarget.dataset["jobId"];
      const jobTitle = event.currentTarget.dataset["jobTitle"];
      const requestOptions = {
        method: "DELETE",
        dataToSend: { jobId: jobId },
        url: deleteJobUrl,
      };
      const msg = confirm(`Do you want to delete ${jobTitle}?`);
      if (msg) {
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            // check if job contains any tasks
            if (data["is_allowed_deleted"] === false) {
              showToastNotification(data["msg"], "info");
            } else {
              showToastNotification(data["msg"], "success");
              setTimeout(() => {
                window.location.reload();
              }, 500);
            }
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      }
    });
  });

  // view job buttons
  managerViewJobBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const jobsUpdateFormWrapper = document.querySelector("div#jobsUpdateFormWrapper");
      const jobsUpdateForm = jobsUpdateFormWrapper.querySelector("form#jobsUpdateForm");
      const jobsUpdateFormFieldSet = jobsUpdateForm.querySelector("fieldset");
      const jobId = event.currentTarget.dataset["jobId"];
      const url = window.localStorage.getItem("RetrieveJobUrl");
      // job-details-update-modal @audit
      const callBacks = {
        onOpenCallBack: () => {
          // console.log("Open update job");
          const requestOptions = {
            method: "POST",
            dataToSend: { jobId: jobId },
            url: url,
          };
          const request = sendRequest(requestOptions);
          request
            .then((data) => {
              // console.log(data);
              const jobObject = data["job"];
              const bookkeepers = jobObject["bookkeeper"];
              const bookkeepersIds = bookkeepers.map((element) => element["id"]);
              const tasks = jobObject["tasks"];
              // console.log(jobObject["client"]);
              jobsUpdateForm["title"].value = jobObject["title"];
              jobsUpdateForm["description"].value = jobObject["description"];
              jobsUpdateForm["due_date"].value = jobObject["due_date"];
              jobsUpdateForm["job_type"].value = jobObject["job_type"];
              jobsUpdateForm["status"].value = jobObject["status"];
              // jobsUpdateForm["client"].value = jobObject["client"];
              jobsUpdateForm["note"].value = jobObject["note"];
              jobsUpdateForm["jobId"].value = jobObject["id"];
              // RadioNodeList: multiple radio inputs,
              // HTMLInputElement: one radio input

              // check the bookkeeper array length
              if (bookkeepersIds.length > 0) {
                // check if the bookkeeper one or more than one input
                if (jobsUpdateForm["bookkeeper"].constructor.name === "HTMLInputElement") {
                  // one input
                  const filtered = bookkeepersIds.some(
                    (ele) => ele == jobsUpdateForm["bookkeeper"].value,
                  );
                  if (filtered === true) {
                    jobsUpdateForm["bookkeeper"].checked = true;
                  }
                } else if (jobsUpdateForm["bookkeeper"].constructor.name === "RadioNodeList") {
                  // two inputs
                  jobsUpdateForm["bookkeeper"].forEach((input) => {
                    const filtered = bookkeepersIds.some((ele) => ele == input.value);
                    // check if filtered is true
                    if (filtered === true) {
                      input.checked = true;
                    }
                  });
                }
              }

              // generate tasks checkbox elements
              if (tasks.length > 0) {
                tasks.forEach((taskElement) => {
                  const fieldElement = document.createElement("div");
                  fieldElement.classList.add(...["field", "jobUpdateTasksField"]);
                  const label = document.createElement("label");
                  label.classList.add(...["checkbox", "is-block", "my-2"]);
                  const taskCheckbox = document.createElement("input");
                  taskCheckbox.type = "checkbox";
                  taskCheckbox.name = "tasks";
                  taskCheckbox.checked = true;
                  taskCheckbox.value = taskElement["id"];
                  taskCheckbox.classList.add(...["mr-1"]);
                  label.textContent = taskElement["title"];
                  label.prepend(taskCheckbox);
                  fieldElement.appendChild(label);
                  jobsUpdateFormFieldSet.appendChild(fieldElement);
                });
              }
              // console.log(tasks);

              /* Array.from(jobsUpdateForm.elements).forEach((element) => {
                console.log(element);
              }); */
              // showToastNotification(data["msg"], "success");
              /* setTimeout(() => {
                window.location.reload();
              }, 500); */
            })
            .catch((error) => {
              console.error(error);
              showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
            })
            .finally(() => {
              jobsFormFieldset.disabled = false;
              managerJobsLoaderBtn.hidden = true;
            });
        },
        onCloseCallback: () => {
          console.warn("Close Update job");
          const allTasksFields = document.querySelectorAll("div.jobUpdateTasksField");
          allTasksFields.forEach((element) => {
            element.remove();
          });
        },
      };
      new MicroModalHandler("job-details-update-modal", callBacks);
      jobsUpdateForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const updateUrl = currentTarget.action;
        const checkedTasks = new Array();
        const checkedBookkeepers = new Array();

        // check if the bookkeeper one or more than one input
        if (currentTarget["bookkeeper"].constructor.name === "HTMLInputElement") {
          // one input
          if (currentTarget["bookkeeper"].checked === true) {
            checkedBookkeepers.push(currentTarget["bookkeeper"].value);
          }
        } else if (currentTarget["bookkeeper"].constructor.name === "RadioNodeList") {
          // two inputs
          currentTarget["bookkeeper"].forEach((input) => {
            if (input.checked === true) {
              checkedBookkeepers.push(input.value);
            }
          });
        }
        // check if the tasks one or more than one input
        if (currentTarget["tasks"].constructor.name === "HTMLInputElement") {
          // one input
          if (currentTarget["tasks"].checked === true) {
            checkedTasks.push(currentTarget["tasks"].value);
          }
        } else if (currentTarget["tasks"].constructor.name === "RadioNodeList") {
          // two inputs
          currentTarget["tasks"].forEach((e) => {
            if (e.checked === true) {
              checkedTasks.push(e.value);
            }
          });
        }

        // console.log("checkedTasks: ", checkedTasks);
        // console.log("checkedBookkeepers: ", checkedBookkeepers);
        const formData = {
          jobId: currentTarget["jobId"].value,
          bookkeeper: checkedBookkeepers,
          tasks: checkedTasks,
          client: currentTarget["client"].value,
          title: currentTarget["title"].value,
          description: currentTarget["description"].value,
          note: currentTarget["note"].value,
          job_type: currentTarget["job_type"].value,
          status: currentTarget["status"].value,
          due_date: currentTarget["due_date"].value,
        };
        console.log(formData);
        const requestOptions = {
          method: "PUT",
          dataToSend: formData,
          url: currentTarget.action,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            showToastNotification("Job updated successfully", "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      });
    });
  });

  // view task buttons
  managerViewTaskBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const taskId = event.currentTarget.dataset["taskId"];
      alert("Work on progress");
    });
  });
  // delete task buttons
  managerDeleteTaskBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const taskId = event.currentTarget.dataset["taskId"];
      alert("Work on progress");
    });
  });
});
