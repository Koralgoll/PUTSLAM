#ifndef _TIME_MEASUREMENT_H
#define _TIME_MEASUREMENT_H

#include <iostream>
#include <fstream>

// Store times
class TimeMeasurement {
public:
	std::vector<long> voTimes, mapTimes, mapAddNewPoseTimes, mapGetSensorPoseTimes, mapGetVisibleFeaturesTimes,
			mapFindNearestFrameTimes, mapRemoveMapFeaturesTimes, mapMoveMapFeaturesToLCSTimes, mapMatchingTimes, mapAddMeasurementTimes;

	void saveToFile() {
		std::ofstream file("times.txt");

		file << "Iter" << "\t"
				<< "voTimes" << "\t"
				<< "mapTimes" << "\t"
				<< "mapAddNewPoseTimes" << "\t"
				<< "mapGetSensorPoseTimes" << "\t"
				<< "mapGetVisibleFeaturesTimes" << "\t"
				<< "mapFindNearestFrameTimes" << "\t"
				<< "mapRemoveMapFeaturesTimes" << "\t"
				<< "mapMoveMapFeaturesToLCSTimes" << "\t"
				<< "mapMatchingTimes" << "\t"
				<< "mapAddMeasurementTimes" << "\t"
				<< std::endl;

		checkAndResizeVectors();

		for (int i = 0; i < voTimes.size(); i++) {
			file << i << "\t"
				<< voTimes[i] << "\t"
				<< mapTimes[i] << "\t"
				<< mapAddNewPoseTimes[i] << "\t"
				<< mapGetSensorPoseTimes[i] << "\t"
				<< mapGetVisibleFeaturesTimes[i] << "\t"
				<< mapFindNearestFrameTimes[i] << "\t"
				<< mapRemoveMapFeaturesTimes[i] << "\t"
				<< mapMoveMapFeaturesToLCSTimes[i] << "\t"
				<< mapMatchingTimes[i] << "\t"
				<< mapAddMeasurementTimes[i] << "\t"
				<< std::endl;
		}

		file << "AVG. " << "\t"
				<< average(voTimes) << "\t"
				<< average(mapTimes) << "\t"
				<< average(mapAddNewPoseTimes) << "\t"
				<< average(mapGetSensorPoseTimes) << "\t"
				<< average(mapGetVisibleFeaturesTimes) << "\t"
				<< average(mapFindNearestFrameTimes)  << "\t"
				<< average(mapRemoveMapFeaturesTimes) << "\t"
				<< average(mapMoveMapFeaturesToLCSTimes) <<"\t"
				<< average(mapMatchingTimes) << "\t"
				<< average(mapAddMeasurementTimes) << "\t"
				<< std::endl;

		file.close();
	}

private:
	double average(std::vector<long> &vec) {
		if (vec.size() == 0)
			return 0.0;

		double s = 0;
		for (auto &v : vec) {
			s += v;
		}
		return s / vec.size();
	}


	void checkAndResizeVectors() {
		int size = voTimes.size();
		mapTimes.resize(size, -1.0);
		mapAddNewPoseTimes.resize(size, -1.0);
		mapGetSensorPoseTimes.resize(size, -1.0);
		mapGetVisibleFeaturesTimes.resize(size, -1.0);
		mapFindNearestFrameTimes.resize(size, -1.0);
		mapRemoveMapFeaturesTimes.resize(size, -1.0);
		mapMoveMapFeaturesToLCSTimes.resize(size, -1.0);
		mapMatchingTimes.resize(size, -1.0);
		mapAddMeasurementTimes.resize(size, -1.0);
	}
};

// Class to measure time
template<typename TimeT = std::chrono::microseconds,
		typename ClockT = std::chrono::high_resolution_clock,
		typename DurationT = double>
class Stopwatch {
private:
	std::chrono::time_point<ClockT> _start, _end;
public:
	Stopwatch() {
		start();
	}
	void start() {
		_start = _end = ClockT::now();
	}
	DurationT stop() {
		_end = ClockT::now();
		return elapsed();
	}
	DurationT elapsed() {
		auto delta = std::chrono::duration_cast < TimeT > (_end - _start);
		return delta.count();
	}
};

#endif // _TIME_MEASUREMENT_H
