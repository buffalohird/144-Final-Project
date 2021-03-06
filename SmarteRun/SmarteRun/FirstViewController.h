#import <UIKit/UIKit.h>
#import <CoreMotion/CoreMotion.h>



double currentMaxAccelX;
double currentMaxAccelY;
double currentMaxAccelZ;
double currentMaxRotX;
double currentMaxRotY;
double currentMaxRotZ;

@interface FirstViewController : UIViewController
@property (strong, nonatomic) IBOutlet UILabel *accX;
@property (strong, nonatomic) IBOutlet UILabel *accY;
@property (strong, nonatomic) IBOutlet UILabel *accZ;

@property (strong, nonatomic) IBOutlet UILabel *maxAccX;
@property (strong, nonatomic) IBOutlet UILabel *maxAccY;
@property (strong, nonatomic) IBOutlet UILabel *maxAccZ;

@property (strong, nonatomic) IBOutlet UILabel *rotX;
@property (strong, nonatomic) IBOutlet UILabel *rotY;
@property (strong, nonatomic) IBOutlet UILabel *rotZ;

@property (strong, nonatomic) IBOutlet UILabel *maxRotX;
@property (strong, nonatomic) IBOutlet UILabel *maxRotY;
@property (strong, nonatomic) IBOutlet UILabel *maxRotZ;

@property (nonatomic) BOOL *isCurrentlyTakingData;
@property (strong, nonatomic) NSTimer *dataLoggingInterval;

@property (nonatomic) double accelerationX;
@property (nonatomic) double accelerationY;
@property (nonatomic) double accelerationZ;

@property (nonatomic, strong) NSMutableArray *xArray;
@property (nonatomic, strong) NSMutableArray *yArray;
@property (nonatomic, strong) NSMutableArray *zArray;







- (IBAction)resetMaxValues:(id)sender;
- (IBAction)logButtonPressed:(id)sender;
- (void)logValues:(id)sender;
- (void)flushAccelerometerData;

@property (strong, nonatomic) CMMotionManager *motionManager;

@end
