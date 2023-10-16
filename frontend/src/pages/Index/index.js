import "../i18n";

import '~/scss/pages/index.scss';

// import '~/assets/images/otter-large.png';
// import '~/assets/images/otter-icon.png';
// import '~/assets/images/otter-portrait.png';
// import '~/assets/images/Alpaca-portrait.png';


window.onload = () => {
  const navDomElement = document.querySelector('nav');
  if (window.pageYOffset == 0) {
    navDomElement.classList.remove('bg-white', 'shadow');
    navDomElement.classList.add('py-3', 'navbar-dark');
  } else {
    navDomElement.classList.remove('opacity-0');
  }
  
  window.addEventListener('scroll', () => {
    if (window.pageYOffset == 0) {
      navDomElement.classList.remove('bg-white', 'shadow');
      navDomElement.classList.add('py-3', 'navbar-dark');
    } else {
      navDomElement.classList.add('bg-white', 'shadow');
      navDomElement.classList.remove('py-3', 'opacity-0', 'navbar-dark');
    }
  });

  const landingDomTitleElement = document.querySelector("#landing .landing-title");
  landingDomTitleElement.classList.add("fade-in-top");
  setTimeout(() => {
    const landingDomSectionsElement = document.querySelector("#landing .landing-sections");
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

const teamDomElement = document.querySelector('#team');
const teamFadeInDomElement = document.querySelector('#team .fade-in');
const teamObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        teamFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
teamObserver.observe(teamDomElement);

const partnersDomElement = document.querySelector('#partners');
const partnersFadeInDomElement = document.querySelector('#partners .fade-in');
const partnersObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        partnersFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
partnersObserver.observe(partnersDomElement);

const btsDomElement = document.querySelector('#behind-the-scenes');
const btsFadeInDomElement = document.querySelector('#behind-the-scenes .fade-in');
const btsObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        btsFadeInDomElement.classList.add("fade-in-left");
      }
    });
  },
  { threshold: 0.5 }
);
btsObserver.observe(btsDomElement);

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
