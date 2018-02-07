var job = document.getElementById("inputGroupJob").value;
var school = document.getElementById("inputGroupSchool").value;
var gender = document.getElementById("inputGroupGender").value;

function getUrl() {
    strURL = job + '/' + school.toLowerCase() + '/' + gender.toLowerCase();
    document.getElementById("search").setAttribute("href", strURL)
}

document.getElementById('search').addEventListener('click', getUrl);