/** @file kinect_grabber.h
 *
 * implementation - Kinect Grabber
 *
 */

#ifndef KINECT_GRABBER_H_INCLUDED
#define KINECT_GRABBER_H_INCLUDED

#include "grabber.h"
#include "../../3rdParty/tinyXML/tinyxml2.h"
#include <iostream>
#include <memory>

namespace putslam {
	/// create a single grabber (Kinect)
	Grabber* createGrabberTemplate(void);
    Grabber* createGrabberTemplate(std::string configFile);
};

using namespace putslam;

/// Grabber implementation
class TemplateGrabber : public Grabber {
    public:

        /// Pointer
        typedef std::unique_ptr<TemplateGrabber> Ptr;

        /// Construction
        TemplateGrabber(void) : Grabber("Kinect Grabber", TYPE_PRIMESENSE, MODE_BUFFER) {};

        /// Construction
        TemplateGrabber(std::string modelFilename) : Grabber("Kinect Grabber", TYPE_PRIMESENSE, Mode::MODE_BUFFER), model(modelFilename){
        }

        /// Name of the grabber
        virtual const std::string& getName() const;

        /// Returns current point cloud
        virtual const PointCloud& getCloud(void) const;

        /// Grab image and/or point cloud
        virtual bool grab();

        /// Calibrate sensor
        virtual void calibrate(void);

        ///Sensor uninitialize
        virtual int grabberClose(void);

        /// Return starting position of sensor
        Eigen::Matrix4f getStartingSensorPose();

    private:
        // Sensor model
        DepthSensorModel model;
};

#endif // KINECT_GRABBER_H_INCLUDED
