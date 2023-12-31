$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.navbar').removeClass('solid');
            $('.navbar').addClass('after-scroll');
        } else {
            $('.navbar').removeClass('after-scroll');
        }
    });
});

function showAlert() {
    $(".emptyalert").show();
    setTimeout(function () {
        $(".emptyalert").hide();
    }, 3000);
}


$(document).ready(function () {
    var input = document.getElementById("searchfield");
    if (input) {
        input.addEventListener("keyup", function (event) {
            event.preventDefault();
            if (event.keyCode == 13) {
                document.getElementById("searchbutton").click();
            }
        })
    }

    $("#searchfield").click(function () {
        $("#searchbutton span i").removeClass("fa-times");
        $("#searchbutton span i").addClass("fa-search");
    });

    $("#searchbutton").click(function () {
        if ($("#searchbutton span i").hasClass("fa-times")) {
            $("#searchresult").html("")
            $("#searchfield").val("");
            $("#searchbutton span i").removeClass("fa-times");
            $("#searchbutton span i").addClass("fa-search");
            $(".searches").css("display", "none");
            // $("#availableitems").css("display", "block");
            var $size = $("#selectpage span").text();
            $.ajax({
                url: "/allitems?page_size=" + $size,
            }).done(function (responses) {
                // console.log(responses);
                res = JSON.parse(responses);
                response = res["response"];
                total_page = res["total_page"]
                var current = res["current"];
                var pages = res["pages"];
                if (response.length > 0) {
                    ht = ""
                    for (var i = 0; i < response.length; i++) {
                        if (response[i]['featured'] == 'true') {
                            ht += '<div class="media border-bottom border-gray d-flex align-items-stretch"><div class="p-2 featured-div mr-2"><span id="featuredSpan"> Featured </span></div><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response[i]["address"] + '</span></div><a href="' + response[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
                        } else {
                            ht += '<div class="media border-bottom border-gray d-flex align-items-stretch no-featured-div"><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response[i]["address"] + '</span></div><a href="' + response[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
                        }
                    }
                    $(".searches").css("display", "block");
                    // $('#searchresult').css("display","block");
                    $("#itemlist").html(ht);
                    $("#pageindex").html("");
                    if (current != 1) {
                        $("#pageindex").append('<a href="" class="pageno">Previous</a>')
                    } else {
                        $("#pageindex").append('<a href="" class="disabled pageno">Previous</a>')
                    }
                    for (var i = 0; i < pages.length; i++) {
                        if (pages[i] == current) {
                            $("#pageindex").append('<a href="" class="active pageno">' + pages[i] + '</a>')
                        } else {
                            $("#pageindex").append('<a href="" class="pageno">' + pages[i] + '</a>')
                        }
                    }
                    if (current != total_page) {
                        $("#pageindex").append('<a class="pageno" href="">Next</a>')
                    } else {
                        $("#pageindex").append('<a class="pageno disabled" href="">Next</a>')
                    }
                    //           $("#pageindex").html("");
                    //           $("#pageindex").append('<a href="" class="disabled pageno">Previous</a>')
                    // //                    ind = '<a href="#" class="disabled">Previous</a>'
                    //           $("#pageindex").append('<a href="" class="active pageno">1</a>')
                    //           for(var j=2; j<total_page+1; j++){
                    //                $("#pageindex").append('<a href="" class="pageno">'+j+'</a>')
                    //           }
                    //           $("#pageindex").append('<a class="pageno" href="">Next</a>')
                }
                $("#availableTitle").text("Available Items (" + res["total_data"] + ")");

            });
        } else {
            var name = $("#searchfield").val();
            var $size = $("#selectpage span").text();
            var name_len = name.replace(/ /g, "").length;
            if (name_len > 0) {
                $.ajax({
                    url: "/searchname?name=" + name + "&size=" + $size,
                }).done(function (response) {
                    all_response = JSON.parse(response);
                    total_page = all_response["total_page"];
                    response = all_response["response"];
                    if (response.length > 0) {
                        ht = ""
                        for (var i = 0; i < response.length; i++) {
                            if (response[i]['featured'] == 'true') {
                                ht += '<div class="media border-bottom border-gray d-flex align-items-stretch"><div class="p-2 featured-div mr-2"><span id="featuredSpan"> Featured </span></div><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response[i]["address"] + '</span></div><a href="' + response[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
                            } else {
                                ht += '<div class="media border-bottom border-gray d-flex align-items-stretch no-featured-div"><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response[i]["address"] + '</span></div><a href="' + response[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
                            }
                        }
                        $(".searches").css("display", "block");
                        $('#searchresult').css("display", "block");
                        $("#itemlist").html(ht);
                        $("#searchbutton span i").removeClass("fa-search");
                        $("#searchbutton span i").addClass("fa-times");
                        // $("#availableitems").css("display", "none");
                        $("#searchfield").blur();
                    } else {
                        var msg = "No results found for <b>" + name + "</b>!<br class='brk'> Please Try again."
                        $("#alertmsg").html(msg);
                        $("#searchfield").val("");
                        $(".searches").css("display", "none");
                        $('#searchresult').css("display", "none");
                        $("#availableitems").css("display", "block");
                        showAlert();
                    }
                    $("#availableTitle").text("Search Results (" + all_response["total_data"] + ")");
                    $("#pageindex").html("");
                    $("#pageindex").append('<a href="" class="disabled pageno">Previous</a>')
                    //                    ind = '<a href="#" class="disabled">Previous</a>'
                    $("#pageindex").append('<a href="" class="active pageno">1</a>')
                    for (var j = 2; j < total_page + 1; j++) {
                        $("#pageindex").append('<a href="" class="pageno">' + j + '</a>')
                    }
                    if (total_page <= 1) {
                        $("#pageindex").append('<a class="disabled pageno" href="">Next</a>')
                    } else {
                        $("#pageindex").append('<a class="pageno" href="">Next</a>')
                    }
                    $(document).scrollTop(0);
                }).fail(function (response) {
                    $("#alertmsg").html("Something went wrong with the search,<br class='brk'> you are redirected to homepage");
                    showAlert();
                    window.setTimeout(function () {
                        window.location = "/";
                    }, 3000);
                });
            } else {
                var msg = "Please write a keyword in order to perform the search"
                $("#searchfield").val("");
                $("#alertmsg").html(msg);
                showAlert();
                $(".searches").css("display", "none");
                $('#searchresult').css("display", "none");
                $("#availableitems").css("display", "block");
            }
        }
    });
});

function get_resp($page, $size, $search, $issizechange = 0) {
    var $page = $page;
    var $size = $size
    var $search = $search
    $.ajax({
        url: "/paginator?pagenumber=" + $page + "&size=" + $size + "&search=" + $search,
    }).done(function (response) {
        // console.log(response);
        var response = JSON.parse(response);
        var response_data = response["response"];
        var total_page = response["total_page"];
        var current = response["current"];
        var pages = response["pages"];
        var ht = ""
        for (var i = 0; i < response_data.length; i++) {
            if (response_data[i]['featured'] == 'true') {
                ht += '<div class="media border-bottom border-gray d-flex align-items-stretch"><div class="p-2 featured-div mr-2"><span id="featuredSpan"> Featured </span></div><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response_data[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response_data[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response_data[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response_data[i]["address"] + '</span></div><a href="' + response_data[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
            } else {
                ht += '<div class="media border-bottom border-gray d-flex align-items-stretch no-featured-div"><div class="align-self-center p-2 img-block-div"><img class="img-thumbnail d-flex align-self-center mr-3" src="' + response_data[i]['image'] + '" width="100px" height="50px"></div><div class="align-self-center p-2 content-div"><div class="text-dark">' + response_data[i]['title'] + '</div><div><img src="static/images/building.png" width="16px" height="16px"><span> ' + response_data[i]['fullname'] + '</span></div><div><img src="static/images/location.png" width="16px" height="16px"><span> ' + response_data[i]["address"] + '</span></div><a href="' + response_data[i]['link'] + '" class="btn btn-outline-success btn-sm" target="_blank">Visit company</a></div></div>'
            }
        }
        $("#itemlist").html("");
        $("#itemlist").html(ht);
        $("#pageindex").html("");
        if (current != 1) {
            $("#pageindex").append('<a href="" class="pageno">Previous</a>')
        } else {
            $("#pageindex").append('<a href="" class="disabled pageno">Previous</a>')
        }
        for (var i = 0; i < pages.length; i++) {
            if (pages[i] == current) {
                $("#pageindex").append('<a href="" class="active pageno">' + pages[i] + '</a>')
            } else {
                $("#pageindex").append('<a href="" class="pageno">' + pages[i] + '</a>')
            }
        }
        if (current != total_page) {
            $("#pageindex").append('<a class="pageno" href="">Next</a>')
        } else {
            $("#pageindex").append('<a class="pageno disabled" href="">Next</a>')
        }
    }).fail(function (response) {
        showAlert();
    })
}

$('.dropdown-menu a').click(function (event) {
    event.preventDefault();
    var $target = $(event.currentTarget);
    var $search = $("#searchfield").val();
    $target.closest('.btn-group')
        .find('[data-bind="label"]').text($target.text())
        .end()
        .children('.dropdown-toggle').dropdown('toggle');
    get_resp(1, $target.text(), $search, 1)

    return false;

});

$(document).ready(function () {
    $(".paginator").on("click", "a.pageno", function (e) {
        e.preventDefault();
        var $search = $("#searchfield").val();
        var $currenteve = $(this).html();
        var $page = $currenteve;
        var $size = $("#selectpage span").text();
        var $parent = $(this);
        var $nextele = $parent.next().html();
        var $prev = "";
        var $nex = "";
        if ($page == "Previous") {
            $page = parseInt($('.paginator a.active')[0].innerText) - 1;
            $parent = $('.paginator a.active').prev();
        }
        if ($page == "Next") {
            $page = parseInt($('.paginator a.active')[0].innerText) + 1;
            $parent = $('.paginator a.active').next();
        }
        $('.paginator a.active').removeClass('active');
        $parent.addClass('active');
        get_resp($page, $size, $search);
        $(document).scrollTop(0);
        if ($page != '1') {
            $(".paginator a:first").removeClass("disabled");
        }
        if ($page == '1') {
            $(".paginator a:first").addClass("disabled");
        }
        if ($('.paginator a.active').next().html() == 'Next') {
            $(".paginator a:last").addClass("disabled");
        } else {
            $(".paginator a:last").removeClass("disabled");
        }
    })
});


// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    const height = Math.max(document.body.scrollHeight, document.body.offsetHeight,
        document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);

    if ((height - document.body.scrollTop) < 1600 || (height - document.documentElement.scrollTop) < 1600) {
        if (document.getElementById("myBtn") !== null) {
            document.getElementById("myBtn").style.display = "block";
        }
    } else {
        if (document.getElementById("myBtn") !== null) {
            document.getElementById("myBtn").style.display = "none";
        }
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


window.addEventListener("load", function () {
    window.cookieconsent.initialise({
        "palette": {
            "popup": {
                "background": "#28a745"
            },
            "button": {
                "background": "#fff",
                "text": "#28a745"
            }
        },
        "content": {
            "href": "/about/cookiepolicy"
        }
    })
});

jQuery(document).ready(function ($) {
    $('.btn-more').on('click', function () {
        $(this).parents('.frm-outer-container').find('.frm-container').slideToggle('slow');
        if ($(this).text() === '+ More')
            $(this).text('- Less');
        else
            $(this).text('+ More');
    });
});

$("button").click(function () {
    $(".sa-success").addClass("hide");
    setTimeout(function () {
        $(".sa-success").removeClass("hide");
    }, 10);
});

$(function () {

    var cities = [
        "Brändö", "Eckerö", "Finström", "Föglö", "Geta", "Hammarland", "Jomala", "Kökar", "Kumlinge", "Lemland", "Lumparland", "Mariehamn", "Saltvik", "Sottunga", "Sund", "Vårdö", "Imatra", "Lappeenranta", "Lemi", "Luumäki", "Parikkala", "Rautjärvi", "Ruokolahti", "Savitaipale", "Taipalsaari", "Ähtäri", "Alajärvi", "Alavus", "Evijärvi", "Ilmajoki", "Isojoki", "Karijoki", "Kauhajoki", "Kauhava", "Kuortane", "Kurikka", "Lappajärvi", "Lapua", "Seinäjoki", "Soini", "Teuva", "Vimpeli", "Enonkoski", "Heinävesi", "Hirvensalmi", "Joroinen", "Juva", "Kangasniemi", "Mäntyharju", "Mikkeli", "Pertunmaa", "Pieksämäki", "Puumala", "Rantasalmi", "Savonlinna", "Sulkava", "Kajaani", "Paltamo", "Ristijärvi", "Sotkamo", "Hyrynsalmi", "Kuhmo", "Puolanka", "Suomussalmi", "Forssa", "Hämeenlinna", "Hattula", "Hausjärvi", "Humppila", "Janakkala", "Jokioinen", "Loppi", "Riihimäki", "Tammela", "Ypäjä", "Halsua", "Kannus", "Kaustinen", "Kokkola", "Lestijärvi", "Perho", "Toholampi", "Veteli", "Äänekoski", "Hankasalmi", "Jämsä", "Joutsa", "Jyväskylä", "Kannonkoski", "Karstula", "Keuruu", "Kinnula", "Kivijärvi", "Konnevesi", "Kuhmoinen", "Kyyjärvi", "Laukaa", "Luhanka", "Multia", "Muurame", "Petäjävesi", "Pihtipudas", "Saarijärvi", "Toivakka", "Uurainen", "Viitasaari", "Hamina", "Iitti", "Kotka", "Kouvola", "Miehikkälä", "Pyhtää", "Virolahti", "Rovaniemi", "Tornio", "Kemi", "Sodankylä", "Keminmaa", "Kemijärvi", "Inari", "Kittilä", "Ylitornio", "Ranua", "Kolari", "Salla", "Pello", "Posio", "Tervola", "Simo", "Muonio", "Enontekiö", "Utsjoki", "Savukoski", "Pelkosenniemi", "Asikkala", "Hartola", "Heinola", "Hollola", "Kärkölä", "Lahti", "Orimattila", "Padasjoki", "Sysmä", "Akaa", "Hämeenkyrö", "Ikaalinen", "Juupajoki", "Kangasala", "Kihniö", "Lempäälä", "Mänttä-Vilppula", "Nokia", "Orivesi", "Pälkäne", "Parkano", "Pirkkala", "Punkalaidun", "Ruovesi", "Sastamala", "Tampere", "Urjala", "Valkeakoski", "Vesilahti", "Virrat", "Ylöjärvi", "Isokyrö", "Jakobstad", "Kaskinen", "Korsholm", "Korsnäs", "Kristinestad", "Kronoby", "Laihia", "Larsmo", "Malax", "Närpes", "Nykarleby", "Pedersöre", "Vaasa", "Vörå", "Ilomantsi", "Joensuu", "Juuka", "Kontiolahti", "Liperi", "Outokumpu", "Polvijärvi", "Kitee", "Rääkkylä", "Tohmajärvi", "Lieksa", "Nurmes", "Valtimo", "Kuusamo", "Taivalkoski", "Haapajärvi", "Kärsämäki", "Nivala", "Pyhäjärvi", "Reisjärvi", "Hailuoto", "Kempele", "Liminka", "Lumijoki", "Muhos", "Oulu", "Tyrnävä", "Ii", "Pudasjärvi", "Utajärvi", "Vaala", "Pyhäjoki", "Raahe", "Siikajoki", "Haapavesi", "Pyhäntä", "Siikalatva", "Alavieska", "Kalajoki", "Merijärvi", "Oulainen", "Sievi", "Ylivieska", "Iisalmi", "Kaavi", "Keitele", "Kiuruvesi", "Kuopio", "Lapinlahti", "Leppävirta", "Pielavesi", "Rautalampi", "Rautavaara", "Siilinjärvi", "Sonkajärvi", "Suonenjoki", "Tervo", "Tuusniemi", "Varkaus", "Vesanto", "Vieremä", "Eura", "Eurajoki", "Harjavalta", "Honkajoki", "Huittinen", "Jämijärvi", "Kankaanpää", "Karvia", "Kokemäki", "Merikarvia", "Nakkila", "Pomarkku", "Pori", "Rauma", "Säkylä", "Siikainen", "Ulvila", "Askola", "Espoo", "Hanko", "Helsinki", "Hyvinkää", "Ingå", "Järvenpää", "Karkkila", "Kauniainen", "Kerava", "Kirkkonummi", "Lapinjärvi", "Lohja", "Loviisa", "Mäntsälä", "Myrskylä", "Nurmijärvi", "Pornainen", "Porvoo", "Pukkila", "Raseborg", "Sipoo", "Siuntio", "Tuusula", "Vantaa", "Vihti", "Aura", "Kaarina", "Kimitoön", "Koski Tl", "Kustavi", "Laitila", "Lieto", "Loimaa", "Marttila", "Masku", "Mynämäki", "Naantali", "Nousiainen", "Oripää", "Paimio", "Pargas", "Pöytyä", "Pyhäranta", "Raisio", "Rusko", "Salo", "Sauvo", "Somero", "Taivassalo", "Turku", "Uusikaupunki", "Vehmaa", "Åland", "Etelä-Karjala", "Etelä-Pohjanmaa", "Etelä-Savo", "Kainuu", "Kanta-Häme", "Keski-Pohjanmaa", "Keski-Suomi", "Kymenlaakso", "Lappi", "Päijät-Häme", "Pirkanmaa", "Pohjanmaa", "Pohjois-Karjala", "Pohjois-Pohjanmaa", "Pohjois-Savo", "Satakunta", "Uusimaa", "Varsinais-Suomi"
    ];

    $("#location").autocomplete({
        source: cities,
        minLength: 2,
        autoFocus: true,
        delay: 0,
    });

    $.ui.autocomplete.filter = function (array, term) {
        var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(term), "i");
        return $.grep(array, function (value) {
            return matcher.test(value.label || value.value || value);
        });
    };
});
