var bio = 
{
	"name" : "Jainil Vachhani",
	"role" : "Software Developer",
	"contacts" :
	{
		"mobile" : "XXX-XXX-XXXX",
		"email" : "jainilvachhani@gmail.com",
		"github" : "jainilvachhani",
		"twitter" : "@jainilvachhani",
		"location" : "ahmedabad"
	},
	"welcomeMessage" : "hello there",
	"skills":
	["awesomeness", "delivering things", "cryogenic sleep", "saving the universe"],
	"bioPic" : "images/fry.jpg"
}

var education = 
{
	"schools" : 
	[
	{
		"name" : "School of Engineering and Applied Sciences",
		"city" : "Ahmedabad",
		"degree" : "Bachelors",
		"majors" : ["ICT"],
		"dates" : 2018,
		"url" : "http://example.com"
	}
	],
	"onlineCourses" : 
	[
		{
			"title" : "JavaScript Crash Course",
			"school" : "Udacity",
			"dates" : 2017,
			"url" : "http://www.udacity.com/course/ud804"
		}
	]	
}

var work = 
{
	"jobs" :
	[
		{
			"employer" : "Indian Institute of Technology",
			"title" : "Research intern",
			"dates" : "May 2016 - July 2016",
			"description" : "worked as research intern"
		}
	]
}

var projects = 
{
	"projects" :
	[
		{
			"title" : "Sample project 1",
			"dates" : "2014",
			"description" : "who moved my cheese",
			"images" : ["http://google.com","http://udacity.com"]
		}
	]
}

var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
    var formattedName = HTMLheaderName.replace("%data%", bio.name);
    var formattedPic = HTMLbioPic.replace("%data%", bio.biopic);

    $("#header").prepend(formattedRole);
    $("#header").prepend(formattedName);
    $("#header").append(formattedPic);

var formattedMobile = HTMLmobile.replace("%data%", bio.contacts.mobile);
var formattedEmail = HTMLemail.replace("%data%", bio.contacts.email);
var formattedTwitter = HTMLtwitter.replace("%data%", bio.contacts.twitter);
var formattedGithub = HTMLgithub.replace("%data%", bio.contacts.github);
var formattedLocation = HTMLlocation.replace("%data%", bio.contacts.location);
	
var contactArray = [];
    contactArray.push(formattedMobile, formattedEmail, formattedTwitter, formattedGithub, formattedLocation);

    // loop thru contacts to display under header

    contactLength = contactArray.length
    for (var i = 0; i < contactLength; i++) {
        $("#topContacts").append(contactArray[i]);
    }

    // loop thru contacts to display in footer

    for (var i = 0; i < contactLength; i++) {
        $("#footerContacts").append(contactArray[i]);
    }
	
	
	
if(bio.skills.length > 0)
{
	$("#header").append(HTMLskillsStart);
	var formattedSkill = HTMLskills.replace("%data%", bio.skills[0]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%", bio.skills[1]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%", bio.skills[2]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%", bio.skills[3]);
	$("#skills").append(formattedSkill);
}

for(job in work.jobs)
{
	$("#workExperience").append(HTMLworkStart);
	var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
	var formattedTitle = HTMLworkTitle.replace("%data%", work.jobs[job].title);
	var formattedEmployerTitle = formattedEmployer + formattedTitle;
	$(".work-entry:last").append(formattedEmployerTitle);
}






for (item in projects.projects) {
        $("#projects").append(HTMLprojectStart);

        var formattedProjectTitle = HTMLprojectTitle.replace("%data%", projects.projects[item].title);
        var formattedProjectDates = HTMLprojectDates.replace("%data%", projects.projects[item].dates);
        var formattedProjectDescription = HTMLprojectDescription.replace("%data%", projects.projects[item].description);
        var formattedProjectImage = HTMLprojectImage.replace("%data%", projects.projects[item].images);
        var projectsURL = projects.projects[item].url;

        // Make Project Title a clickable link
        var formattedProjectTitle = formattedProjectTitle.replace("#", projectsURL);

        // create projects array to loop over
        var projectsArray = [];
        projectsArray.push(formattedProjectTitle, formattedProjectDates, formattedProjectDescription, formattedProjectImage);
        var projectsLength = projectsArray.length;

        // loop over projects array
        for (var i = 0; i < projectsLength; i++) {
            $(".project-entry:last").append(projectsArray[i]);
        }
    }
	
	
	
	$("#education").append(HTMLschoolStart);
    for (school in education.schools) {

        var formattedSchoolName = HTMLschoolName.replace("%data%", education.schools[school].name);
        var formattedSchoolDegree = HTMLschoolDegree.replace("%data%", education.schools[school].degree);
        var formattedSchoolDates = HTMLschoolDates.replace("%data%", education.schools[school].dates);
        var formattedSchoolLocation = HTMLschoolLocation.replace("%data%", education.schools[school].location);
        var formattedSchoolMajor = HTMLschoolMajor.replace("%data%", education.schools[school].majors);
        var educationURL = education.schools[school].url;

        // concat school name and degree obtained
        var formattedSchoolNameFinal = formattedSchoolName + formattedSchoolDegree;

        // make school name a clickable link
        var formattedSchoolNameFinal = formattedSchoolNameFinal.replace("#", educationURL);

        // create education array to loop over
        var educationArray = [];
        educationArray.push(formattedSchoolMajor, formattedSchoolLocation, formattedSchoolDates, formattedSchoolNameFinal);
        var educationLength = educationArray.length;

        // loop over education array
        for (var i = 0; i < educationLength; i++) {
            $(".education-entry:last").prepend(educationArray[i]);
        }
    }

    // start online courses section
    $(".education-entry:last").append(HTMLonlineClasses);
    for (moocs in education.onlineCourses) {

        var formattedOnlineTitle = HTMLonlineTitle.replace("%data%", education.onlineCourses[moocs].title);
        var formattedOnlineSchool = HTMLonlineSchool.replace("%data%", education.onlineCourses[moocs].school);
        var formattedOnlineDates = HTMLonlineDates.replace("%data%", education.onlineCourses[moocs].date);
        var formattedOnlineURL = HTMLonlineURL.replace("%data%", education.onlineCourses[moocs].url);

        // make url strings clickable links
        var formattedOnlineURL = formattedOnlineURL.replace("#", education.onlineCourses[moocs].url);

        // concat course title and university name
        var formattedOnlineProvider = formattedOnlineTitle + formattedOnlineSchool;

        // make course titles clickable links
        var formattedOnlineProvider = formattedOnlineProvider.replace("#", education.onlineCourses[moocs].url);

        // create moocs array to loop over
        var moocsArray = [];
        moocsArray.push(formattedOnlineProvider, formattedOnlineDates, formattedOnlineURL);
        moocsLength = moocsArray.length;

        // loop over moocs array
        for (var i = 0; i < moocsLength; i++) {
            $(".education-entry:last").append(moocsArray[i]);
        }
    }
	
	
	
	$("#mapDiv").append(googleMap);
	
	