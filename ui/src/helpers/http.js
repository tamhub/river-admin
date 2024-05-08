import { BASE_URL } from "@/helpers/constants";
import { CAN_NOT_DELETE_DUE_TO_PROTECTION } from "@/helpers/errors";
import { emit_error } from "@/helpers/event_bus";
import store from "@/store";
import axios from "axios";

const getHeaders = () => ({
  Authorization: `Bearer ${store.state.user.token}`,
});

class Http {
  _request(options, callback) {
    const axios_options = {
      ...options,
      url: `${BASE_URL}${options.url}`,
    };
    return axios(axios_options)
      .then(callback)
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 401 || error.response.status === 403) {
            console.log("401 or 403", error.response, getHeaders());
            // emit_logout();
          } else {
            this.handle_error(error.response);
          }
        } else {
          console.error(error);
        }
      });
  }

  get(url, callback) {
    return this._request(
      { method: "get", url, headers: getHeaders() },
      callback
    );
  }
  post(url, data, callback) {
    return this._request(
      { method: "post", url, data, headers: getHeaders() },
      callback
    );
  }

  put(url, data, callback) {
    return this._request(
      { method: "put", url, data, headers: getHeaders() },
      callback
    );
  }
  patch(url, data, callback) {
    return this._request(
      { method: "patch", url, data, headers: getHeaders() },
      callback
    );
  }

  delete(url, callback) {
    return this._request(
      { method: "delete", url, headers: getHeaders() },
      callback
    );
  }

  handle_error(error) {
    if (error.status === 400) {
      error.data.forEach((err) => {
        switch (err.error_code) {
          case CAN_NOT_DELETE_DUE_TO_PROTECTION:
            emit_error(this.build_protection_error_messages(err));
            break;
          default:
            console.log(
              `An unexpected error occured with the code ${err.error_code}`
            );
        }
      });
    }
  }

  build_protection_error_messages(error) {
    return new Set(
      error.detail.protected_errors.map((protected_error) => {
        var dependency_name = "";
        switch (protected_error.object_type) {
          case "workflow":
            dependency_name = "workflow";
            break;
          case "state":
            dependency_name = "state";
            break;
          case "transitionmeta":
            dependency_name = "transition meta";
            break;
          case "transitionapprovalmeta":
            dependency_name = "transition approval meta";
            break;
          case "transition":
            dependency_name = "transition";
            break;
          case "transitionapproval":
            dependency_name = "transition approval";
            break;
          case "ontransitionhook":
            dependency_name = "transition hook";
            break;
          case "onapprovedhook":
            dependency_name = "approval hook";
            break;
          default:
            console.error(
              `Unexpected protected object type ${protected_error.object_type}`
            );
            return null;
        }
        return `Can not delete since there is a dependant ${dependency_name} object`;
      })
    );
  }
}
var http = new Http();
export default http;
