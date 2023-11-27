function selectHoliday(holiday) {
  document.getElementById("holidayDropdown").innerText = holiday;
  document.getElementById("{{ form.tags.id_for_label }}").value = holiday;
}

