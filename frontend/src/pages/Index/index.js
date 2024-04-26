import React from "react";
import { createRoot } from "react-dom/client";

import "../i18n";

import ProjectsApp from "./containers/ProjectsApp";

import '~/scss/pages/index.scss';

import '~/assets/images/blackbox_logo.png';
import '~/assets/images/hariken_logo.png';
import '~/assets/images/jnc-nina_logo.png';
import '~/assets/images/naban_logo.png';
import '~/assets/images/nazca-editions_logo.jpg';
import '~/assets/images/piccoma_logo.png';
import '~/assets/images/taicca_logo.png';
import '~/assets/images/izneo_logo.png';
import '~/assets/images/mangasio_logo.svg';

import '~/assets/images/studio-img_1.svg';
import '~/assets/images/studio-img_2.svg';
import '~/assets/images/studio-img_3.svg';
import '~/assets/images/studio-img_4.svg';
import '~/assets/images/studio-img_5.svg';


$("body").css("background", `fixed no-repeat center url(${LANDING_BANNER})`);
$("body").css("background-size", "auto 100vh");
$("#landing").css("background", "rgba(0, 0, 0, 50%");

window.onload = () => {
  const navDomElement = document.querySelector('nav');
  if (window.pageYOffset == 0) {
    navDomElement.classList.remove('bg-white', 'shadow');
    navDomElement.classList.add('py-3', 'navbar-dark', 'blurred-background');
  } else {
    navDomElement.classList.remove('opacity-0');
  }
  
  window.addEventListener('scroll', () => {
    if (window.pageYOffset == 0) {
      navDomElement.classList.remove('bg-white', 'shadow');
      navDomElement.classList.add('py-3', 'navbar-dark');
      setTimeout(() => { navDomElement.classList.add('blurred-background'); }, 50);
    } else {
      navDomElement.classList.add('bg-white', 'shadow');
      navDomElement.classList.remove('py-3', 'opacity-0', 'navbar-dark', 'blurred-background');
    }
  });

  const landingDomTitleElement = document.querySelector("#landing .landing-title");
  landingDomTitleElement.classList.add("fade-in-top");
  setTimeout(() => {
    const landingDomSectionsElement = document.querySelector("#landing #landing-sections");
    landingDomSectionsElement.classList.add("fade-in-bottom");
  }, 500);
  setTimeout(() => {
    navDomElement.classList.remove('opacity-0');
  }, 1500);
};

const studioDomElement = document.querySelector('#studio');
const studioFadeInDomElement = document.querySelector('#studio .fade-in');
const studioObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        studioFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
studioObserver.observe(studioDomElement);

const projectsDomElement = document.querySelector('#projects');
const projectsFadeInDomElement = document.querySelector('#projects .fade-in');
const projectsObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        projectsFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
projectsObserver.observe(projectsDomElement);

const theyTrustUsDomElement = document.querySelector('#they-trust-us');
const theyTrustUsFadeInDomElement = document.querySelector('#they-trust-us .fade-in');
const theyTrustUsObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        theyTrustUsFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
theyTrustUsObserver.observe(theyTrustUsDomElement);

const contactDomElement = document.querySelector('#contact');
const contactFadeInDomElement = document.querySelector('#contact .fade-in');
const contactObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        contactFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
contactObserver.observe(contactDomElement);


/* === PARTNERS ANIMATIONS === */
const partners = $("#partners");
const firstScrollDiv = partners.children()[0];

const clonedMembers3ia = partners.clone(); // CLONING CONTAINER FOR INFINITE REPEAT
const secondScrollDiv = clonedMembers3ia.children()[0];
partners.parent().append(clonedMembers3ia);

const initPositions = () => {
    firstScrollDiv.style.transform = `translateX(0px)`;
    secondScrollDiv.style.transform = `translateX(${firstScrollDiv.scrollWidth}px)`;
};

// SCROLL FUNCTION
let scrollPosition = 0;
const scrollLoop = ({scrollSpeed = 1}) => {
      scrollPosition += scrollSpeed;
      if (scrollPosition > firstScrollDiv.scrollWidth) {
          scrollPosition = 0;
          firstScrollDiv.style.transform = `translateX(-${scrollPosition}px)`;
          secondScrollDiv.style.transform = `translateX(${firstScrollDiv.scrollWidth - scrollPosition}px)`;
      }
      firstScrollDiv.style.transform = `translateX(-${scrollPosition}px)`;
      secondScrollDiv.style.transform = `translateX(${firstScrollDiv.scrollWidth - scrollPosition}px)`;
    
      requestAnimationFrame(scrollLoop);
};

$(window).on("resize", () => { initPositions(); });

initPositions();

// Start the continuous scroll loop
scrollLoop({ scrollSpeed: 1 });

createRoot(document.getElementById("projects-app")).render(
  <ProjectsApp
    projects = { PROJECTS }
  />
);