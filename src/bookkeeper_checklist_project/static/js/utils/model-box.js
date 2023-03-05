"use strict";

const showMicroModal = (modalId, onCloseCallback, onOpenCallBack) => {
  MicroModal.show(modalId, {
    disableScroll: false,
    onClose: (modal) => {
      //   console.info(`${modal.id} is hidden`);
      if (typeof onCloseCallback == "function") {
        onCloseCallback();
      }
    },
    onShow: (modal) => {
      //   console.info(`${modal.id} is hidden`);
      if (typeof onOpenCallBack == "function") {
        onOpenCallBack();
      }
    },

    disableFocus: false,
  });
};

class MicroModalHandler {
  constructor(modalId, callBacks) {
    this.modalId = modalId;
    if (typeof callBacks["onCloseCallback"] == "function") {
      this.onCloseCallback = callBacks["onCloseCallback"];
    }
    if (typeof callBacks["onOpenCallBack"] == "function") {
      this.onOpenCallBack = callBacks["onOpenCallBack"];
    }

    this.fireModal();
  }

  fireModal() {
    MicroModal.show(this.modalId, {
      disableScroll: false,
      onClose: (modal) => {
        //   console.info(`${modal.id} is hidden`);
        if (typeof this.onCloseCallback == "function") {
          this.onCloseCallback();
        }
      },
      onShow: (modal) => {
        //   console.info(`${modal.id} is hidden`);
        if (typeof this.onOpenCallBack == "function") {
          this.onOpenCallBack();
        }
      },

      disableFocus: false,
    });
  }
}

// class MicroModalHandlerV2 {
class TingleModalHandler {
  constructor(modalId, callBacks) {
    this.modalId = modalId;
    // console.log(typeof callBacks["onCloseCallback"]);
    // callBacks["onCloseCallback"]();
    if (typeof callBacks["onCloseCallback"] == "function") {
      this.onCloseCallback = callBacks["onCloseCallback"];
    }
    if (typeof callBacks["onOpenCallBack"] == "function") {
      this.onOpenCallBack = callBacks["onOpenCallBack"];
    }
    if (typeof callBacks["onBeforeClose"] == "function") {
      this.onBeforeClose = callBacks["onBeforeClose"];
    }
    if (typeof callBacks["beforeOpen"] == "function") {
      this.beforeOpen = callBacks["beforeOpen"];
    }
    // console.log(callBacks);
    this.fireModal();
  }

  fireModal() {
    const modalOptions = {
      footer: true,
      stickyFooter: true,
      // closeMethods: ["overlay", "button", "escape"],
      closeMethods: ["button", "escape"],
      closeLabel: "Close",
    };
    if (this.onOpenCallBack) {
      modalOptions["onOpen"] = this.onOpenCallBack;
    }
    if (this.onCloseCallback) {
      modalOptions["onClose"] = this.onCloseCallback;
    }
    if (this.onBeforeClose) {
      modalOptions["beforeClose"] = this.onBeforeClose;
    }
    if (this.beforeOpen) {
      modalOptions["beforeOpen"] = this.beforeOpen;
    }
    const modal = new tingle.modal(modalOptions);
    modal.setContent(document.querySelector(`#${this.modalId}`).innerHTML);
    modal.addFooterBtn("Submit", "button tingle-btn--pull-right is-responsive is-primary", () => {
      alert("click on primary button!");
      const formElement = document.querySelector(`#${this.modalId}`).querySelector("form");
      // console.log(formElement);
    });

    /* modal.addFooterBtn(
      "Cancel",
      "tingle-btn tingle-btn--default tingle-btn--pull-right",
      function () {
        modal.close();
      },
    ); */

    modal.addFooterBtn("Cancel", "button is-responsive is-danger", () => {
      // alert("click on danger button!");
      modal.close();
    });
    modal.open();
  }
}

export { showMicroModal, MicroModalHandler, TingleModalHandler };
