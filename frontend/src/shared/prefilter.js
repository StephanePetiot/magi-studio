import Cookies from "js-cookie";

const csrftoken = Cookies.get("csrftoken");

// Works for all $.ajax() calls
$.ajaxPrefilter( (settings, original, xhr) => {
    xhr.withCredentials = true;
    if (['post','put','delete'].includes(settings.type.toLowerCase()) && !settings.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

// Works for all $.ajax() calls and $.get(), $.post(), etc. calls (BUT NOT RECOMMENDED)
$.ajaxSetup({
    beforeSend: (xhr, settings) => {
        if (['post','put','delete'].includes(settings.type.toLowerCase()) && !settings.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
