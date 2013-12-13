/** @file transformEst.h
 *
 * Feature-based transformation estimation interface
 *
 */

#ifndef _TRANSFORMEST_H_
#define _TRANSFORMEST_H_

#include "../Defs/putslam_defs.h"
#include <string>
#include <vector>

namespace putslam {
    /// Transformation Estimator interface
    class TransformEst {
        public:

            /// Name of the estimator
            virtual const std::string& getName() const = 0;

            /// Returns current transformation
            virtual const Mat34& getTransformation(void) const = 0;

            /// Grab image and/or point cloud
            virtual void computeTransformation(ImageFeature::Seq& keypointA, ImageFeature::Seq& keypointB) = 0;

            /// Virtual descrutor
            virtual ~TransformEst() {}
    };
};

#endif // _TRANSFORMEST_H_
