#include <memory>
#include <stdexcept>
#include <chrono>
#include <thread>
#include "../../include/Grabber/templateGrabber.h"

using namespace putslam;

/// A single instance of Kinect grabber
TemplateGrabber::Ptr grabberK;

const std::string& TemplateGrabber::getName() const {
	return name;
}

const PointCloud& TemplateGrabber::getCloud(void) const {
    return cloud;
}

bool TemplateGrabber::grab(void) {
    Point3D point;
    point.r = 255; point.g = 0; point.b = 0; point.a = 255;
    point.x = 1.2; point.y = 3.4; point.z = 5.6;
	cloud.push_back(point);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    return true;
}

/// run grabber thread
void TemplateGrabber::calibrate(void) {

}

int TemplateGrabber::grabberClose(){
    return 0;
}

Eigen::Matrix4f TemplateGrabber::getStartingSensorPose()
{
	Eigen::Matrix4f::Identity();
}

putslam::Grabber* putslam::createGrabberTemplate(void) {
    grabberK.reset(new TemplateGrabber());
    return grabberK.get();
}

putslam::Grabber* putslam::createGrabberTemplate(std::string configFile) {
    grabberK.reset(new TemplateGrabber(configFile));
    return grabberK.get();
}

