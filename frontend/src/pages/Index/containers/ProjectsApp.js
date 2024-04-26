import React from "react";
import PropTypes from "prop-types";

import ProjectComponent from "../components/ProjectComponent/ProjectComponent";

const ProjectsApp = (props) => {
    
    return <div
        className = "py-5 overflow-auto"
        style = {{ whiteSpace: "nowrap" }}
    >
        {
            props.projects.map((item, i) => {
                return <ProjectComponent key = { i } { ...item } />;
            })
        }
    </div>;
};

ProjectsApp.propTypes = {
    projects: PropTypes.arrayOf(PropTypes.object)
};

export default ProjectsApp;