$(document).ready(function () {
  $(function () {
    /*refresh detection algorithm*/
    checkRefresh();
    /* end of algorithm */

    /*drop down animation start */
    $("#b_state").on("click", function () {
      $("#s_state").slideDown(500);
    });

    $("#s_state").on("click", function () {
      $("#s_state").slideUp(0);
    });

    $("#b_district").on("click", function () {
      $("#s_district").slideDown(500);
    });

    $("#s_district").on("click", function () {
      $("#s_district").slideUp(0);
    });
    $("#b_taluka").on("click", function () {
      $("#s_taluka").slideDown(500);
    });

    $("#s_taluka").on("click", function () {
      $("#s_taluka").slideUp(0);
    });
    /*drop down animation end */

    /*To active Navigation links*/
    $("nav li a")
      .filter(function () {
        return this.href === location.href;
      })
      .addClass("active");
  });
  /*end Navigation links*/

  $(document).on("click", ".dropdown-state", function () {
    obj = $(this);
    state_id = obj.attr("data-state-id");
    url = obj.attr("url");
    districtUrl = obj.attr("district-url");
    data = {
      state_id: state_id,
    };
    getAPIData(data, url);
    filterDistricts(data, districtUrl);

    /*Add text on Dropdown button*/
    text = obj.text();
    $("#b_state").text(text);

    /* setting session variable for pagination*/
    sessionStorage.setItem("state_id", state_id);
  });

  $(document).on("click", ".dropdown-district", function () {
    obj = $(this);
    district_id = obj.attr("data-district-id");
    url = obj.attr("url");
    talukaUrl = obj.attr("taluka-url");
    data = {
      district_id: district_id,
    };
    getAPIData(data, url);
    filterTalukas(data, talukaUrl);

    /*Add text on Dropdown button*/
    text = obj.text();
    $("#b_district").text(text);

    /* setting session variable for pagination*/
    sessionStorage.setItem("district_id", district_id);
  });

  $(document).on("click", ".dropdown-taluka", function () {
    obj = $(this);
    taluka_id = obj.attr("data-taluka-id");
    url = obj.attr("url");
    data = {
      taluka_id: taluka_id,
    };
    getAPIData(data, url);

    /*Add text on Dropdown button*/
    text = obj.text();
    $("#b_taluka").text(text);

    /* setting session variable for pagination*/
    sessionStorage.setItem("taluka_id", taluka_id);
  });

  /*on Click Edit Button*/
  $(document).on("click", ".editbtn", function () {
    obj = $(this);
    hospital_id = obj.attr("id");
    editUrl = obj.attr("edit-url");
    data = {
      hospital_id: hospital_id,
    };
    editHospitalBeds(data, editUrl);
  });

  $(document).on("click", "#list_next", function () {
    console.log("next clicked");
    obj = $(this);
    data = {
      page: obj.attr("page"),
    };
    url = "/hospital/";
    if (sessionStorage.getItem("taluka_id")) {
      data.taluka_id = sessionStorage.getItem("taluka_id");
      getAPIData(data, url);
    } else if (sessionStorage.getItem("district_id")) {
      data.district_id = sessionStorage.getItem("district_id");
      getAPIData(data, url);
    } else if (sessionStorage.getItem("state_id")) {
      data.state_id = sessionStorage.getItem("state_id");
      getAPIData(data, url);
    }
  });

  $(document).on("click", "#list_prev", function () {
    obj = $(this);
    data = {
      page: obj.attr("page"),
    };
    url = "/hospital/";
    if (sessionStorage.getItem("taluka_id")) {
      data.taluka_id = sessionStorage.getItem("taluka_id");
      getAPIData(data, url);
    } else if (sessionStorage.getItem("district_id")) {
      data.district_id = sessionStorage.getItem("district_id");
      getAPIData(data, url);
    } else if (sessionStorage.getItem("state_id")) {
      data.state_id = sessionStorage.getItem("state_id");
      getAPIData(data, url);
    }
  });
});

function getAPIData(data, url) {
  $.ajax({
    method: "GET",
    url: url,
    data: data,
    success: function (result) {
      $("#hospital_table").html(result);
    },
  });
}

function filterDistricts(data, url) {
  $.ajax({
    method: "GET",
    url: url,
    data: data,
    success: function (result) {
      $("#filter_district").html(result);
    },
  });
}

function filterTalukas(data, url) {
  $.ajax({
    method: "GET",
    url: url,
    data: data,
    success: function (result) {
      $("#filter_taluka").html(result);
    },
  });
}

function editHospitalBeds(data, url) {
  pk = data.hospital_id;
  $.ajax({
    method: "GET",
    url: url,
    data: data,
    success: function (result) {
      $("#hospital-" + pk).html(result);
      $("label").text(""); // to remove `Bed_Available` text from box
    },
  });
}

/* for csrf token issue in django+ajax */
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  },
});

/* refresh detection algorithm */
function checkRefresh() {
  if (document.refreshForm.visited.value == "") {
    // This is a fresh page load
    // You may want to add code here special for
    // fresh page loads
    document.refreshForm.visited.value = "1";
    sessionStorage.clear();
  } else {
    // This is a ajax call
    // Insert code here representing what to do on
    // a refresh
    // nothing to add for now
  }
}

/* On Click Update Button 
  will come back on validation feature
  must be written inside document.on-ready
*/
// $(document).on("click", "#updatebtn", function () {
//   obj = $(this);
//   hospital_id = obj.attr("data-id");
//   data = {
//     hospital_id: hospital_id,
//   };
//   updateHospitalBeds(data);
// });

/* and this one outside document-on-ready */
// function updateHospitalBeds(data) {
//   pk = data.hospital_id;
//   let url = "http://127.0.0.1:8000/hospital_update/" + pk + "/";

//   $.ajax({
//     method: "POST",
//     url: url,
//     data: data,
//   });
// }
