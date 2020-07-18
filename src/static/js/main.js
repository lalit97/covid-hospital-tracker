$(document).ready(function () {
  $(function () {
    // $("#b_state").on("click", function () {
    //   $(".dropdown-menu a").slideToggle(280);
    // });

    /*To active Navigation buttons*/
    $("nav li a")
      .filter(function () {
        return this.href === location.href;
      })
      .addClass("active");
  });
  $(".dropdown-state").click(function () {
    obj = $(this);
    state_id = obj.attr("data-state-id");
    console.log(state_id);
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
  });

  $(".dropdown-district").click(function () {
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
  });

  $(".dropdown-taluka").click(function () {
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
  });

  /*on Click Edit Button*/
  $(".editbtn").click(function () {
    obj = $(this);
    hospital_id = obj.attr("id");
    editUrl = obj.attr("edit-url");
    data = {
      hospital_id: hospital_id,
    };
    editHospitalBeds(data, editUrl);
  });

  /* On Click Update Button 
    will come back on validation feature
  */
  // $(document).on("click", "#updatebtn", function () {
  //   console.log("clicked now");
  //   obj = $(this);
  //   hospital_id = obj.attr("data-id");
  //   data = {
  //     hospital_id: hospital_id,
  //   };
  //   updateHospitalBeds(data);
  // });
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

// function updateHospitalBeds(data) {
//   pk = data.hospital_id;
//   let url = "http://127.0.0.1:8000/hospital_update/" + pk + "/";

//   $.ajax({
//     method: "POST",
//     url: url,
//     data: data,
//   });
// }

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
