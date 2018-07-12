#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>
#include <std_msgs/Float32.h>

#define echoPin 7
#define trigPin 8

float duration, cm;
float maximum_range=400;
float minimum_range=2;
//sensor_msgs::Range sonar_msg;
std_msgs::Float32 sonar_msg;
ros::Publisher pub_sonar("sonar", &sonar_msg);
ros::NodeHandle nh;
//char frameid[] = "/ultrasound";
void setup()
{

  nh.initNode();
  nh.advertise(pub_sonar);
  
//    sonar_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
//  sonar_msg.header.frame_id =  frameid;
 // sonar_msg.field_of_view = 0.01;
// sonar_msg.min_range = 2;
//  sonar_msg.max_range = 400;
  
pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}


long publisher_timer;

float getRange(int echo, int trig){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  
  // convert the time into a distance
  cm = (duration/2)/29.1;
  if(cm >= 400||cm <= 2){
    return -1.0;
  }
  return cm;
}

void loop()
{

  if ( (millis()>=publisher_timer)){
  sonar_msg.data = (int)getRange(echoPin,trigPin);
//  sonar_msg.header.stamp = nh.now();
  pub_sonar.publish(&sonar_msg);

  publisher_timer = millis() + 50; //publish once a second

  }

  nh.spinOnce();
}
