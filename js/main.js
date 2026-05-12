(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    if ($('.page-header').length > 0) {
        // Pagine interne: navbar sempre visibile
        $('.sticky-top').css('top', '0px');
        $(window).scroll(function () {
            if ($(this).scrollTop() > 50) {
                $('.sticky-top').addClass('shadow-sm');
            } else {
                $('.sticky-top').removeClass('shadow-sm');
            }
        });
    } else {
        // Homepage: navbar appare dopo 300px di scroll
        $(window).scroll(function () {
            if ($(this).scrollTop() > 300) {
                $('.sticky-top').addClass('shadow-sm').css('top', '0px');
            } else {
                $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
            }
        });
    }
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        loop: true,
        nav: false,
        dots: false,
        items: 1,
    });


    // Testimonials carousel
    $('.testimonial-carousel').owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        loop: true,
        nav: false,
        dots: true,
        items: 1,
        dotsData: true,
    });

    // Cookie Consent Banner
    if (!localStorage.getItem('cookieConsent')) {
        var bannerHTML = `
            <div id="cookie-consent-banner">
                <p>Utilizziamo esclusivamente cookie tecnici per garantire il corretto funzionamento del sito. Non effettuiamo profilazione. Puoi accettare o rifiutare l'utilizzo dei cookie.</p>
                <div class="btn-container">
                    <button id="btn-accept-cookie" class="btn btn-primary btn-sm">Accetta</button>
                    <button id="btn-reject-cookie" class="btn btn-secondary btn-sm" style="background-color:#555; color:#fff; border:none;">Rifiuta</button>
                </div>
            </div>
        `;
        $('body').append(bannerHTML);

        $('#btn-accept-cookie').click(function () {
            localStorage.setItem('cookieConsent', 'accepted');
            $('#cookie-consent-banner').fadeOut('fast', function() { $(this).remove(); });
        });

        $('#btn-reject-cookie').click(function () {
            localStorage.setItem('cookieConsent', 'rejected');
            $('#cookie-consent-banner').fadeOut('fast', function() { $(this).remove(); });
        });
    }

})(jQuery);
