import React from "react";
import PropTypes from "prop-types";

const ProjectComponent = (props) => {
    return <div className = "project-card card w-100">
        <div className = "bordered-container">
            <div className = "inner-bordered-container">
                <div className = "card-body" style = {{ minHeight: "100px" }}>
                    <div className = "card-title fs-4 fw-bold">{ props.title.toUpperCase() }</div>
                    <div className = "card-subtitle fs-5">{ props.subtitle }</div>
                </div>
                <div className = "project-card-bottom overflow-hidden position-relative shine">
                    <img className = "card-img-bottom align-bottom" src = { props.picture ? props.picture : null } />
                    <div className = "project-card-img-overlay position-absolute top-0 bottom-0 start-0 end-0"></div>
                    <p className = "project-card-text text-light fw-bold fs-5 position-absolute top-0 bottom-0 start-0 end-0 p-3 text-wrap overflow-auto">
                        { props.description }
                    </p>
                </div>
            </div>
        </div>
    </div>;
};

ProjectComponent.propTypes = {
    title: PropTypes.string,
    subtitle: PropTypes.string,
    description: PropTypes.string,
    picture: PropTypes.string
};

export default ProjectComponent;