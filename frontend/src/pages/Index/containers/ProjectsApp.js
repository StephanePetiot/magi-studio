import React from "react";
import PropTypes from "prop-types";
import { Swiper, SwiperSlide } from 'swiper/react';
import { Grid, Pagination, Navigation } from 'swiper/modules';

import ProjectComponent from "../components/ProjectComponent/ProjectComponent";

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/grid';
import 'swiper/css/pagination';
import 'swiper/css/navigation';


const ProjectsApp = (props) => {
    
    return <>
     <Swiper
            slidesPerView={1}
            breakpoints={{
                480: {
                    slidesPerView: 2,
                    spaceBetween: 50,
                    grid: {
                        rows: 2,
                        fill: "row"
                    }
                },
                640: {
                    slidesPerView: 3,
                    spaceBetween: 40,
                    grid: {
                        rows: 2,
                        fill: "row"
                    }
                },
                800: {
                    slidesPerView: 4,
                    spaceBetween: 30,
                    grid: {
                        rows: 2,
                        fill: "row"
                    }
                }
            }}
            grid={{
                rows: 2,
                fill: "row"
            }}
            spaceBetween={30}
            pagination={{
                dynamicBullets: true,
            }}
            navigation={{
                nextEl: '.custom-swiper-button-next',
                prevEl: '.custom-swiper-button-prev',
            }}
            modules={[Grid, Pagination, Navigation]}
            className = "my-3"
            style = {{ paddingBottom: "50px" }}
        >
            {
                props.projects.map((item, i) => {
                    return <SwiperSlide className="d-flex justify-content-center align-items-center" key = { i }>
                        <ProjectComponent { ...item } />
                    </SwiperSlide>;
                })
            }
        </Swiper>
     </>;
};

ProjectsApp.propTypes = {
    projects: PropTypes.arrayOf(PropTypes.object)
};

export default ProjectsApp;