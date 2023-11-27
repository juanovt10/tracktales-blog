function selectHoliday(holiday) {
  document.getElementById("holidayDropdown").innerText = holiday;
  document.getElementById("{{ form.tags.id_for_label }}").value = holiday;
}


function selectArea(area) {
    document.getElementById("areaDropdown").innerText = area;
    document.getElementById("{{ form.area.id_for_label }}").value = holiday;
}