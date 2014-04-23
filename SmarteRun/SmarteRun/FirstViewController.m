//
//  FirstViewController.m
//  SmarteRun
//
//  Created by Buffalo Hird on 4/15/14.
//  Copyright (c) 2014 Buffalo Hird. All rights reserved.
//

#import "FirstViewController.h"



@interface FirstViewController ()

@end

@implementation FirstViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    NSLog(@"perry wants it in the cookie jar");
	// Do any additional setup after loading the view, typically from a nib.
    
    self.isCurrentlyTakingData = NO;
    
    currentMaxAccelX = 0;
    currentMaxAccelY = 0;
    currentMaxAccelZ = 0;
    
    currentMaxRotX = 0;
    currentMaxRotY = 0;
    currentMaxRotZ = 0;
    
    self.xArray = [[NSMutableArray alloc] init];
    self.yArray = [[NSMutableArray alloc] init];
    self.zArray = [[NSMutableArray alloc] init];
    
}

-(IBAction)logButtonPressed:(id)sender
{
    if (!self.isCurrentlyTakingData)
    {
        self.isCurrentlyTakingData = YES;
        [self.motionManager startAccelerometerUpdatesToQueue:[NSOperationQueue currentQueue]
                                                 withHandler:^(CMAccelerometerData  *accelerometerData, NSError *error) {
                                                     [self outputAccelerationData:accelerometerData.acceleration];
                                                     if(error){
                                                         
                                                         NSLog(@"%@", error);
                                                     }
                                                 }];
        
        self.dataLoggingInterval = [NSTimer scheduledTimerWithTimeInterval:0.2
                                         target:self
                                       selector:@selector(logValues:)
                                       userInfo:nil
                                        repeats:YES];
        
    }
    else
    {
        self.isCurrentlyTakingData = NO;
        [self flushAccelerometerData];
        [self.dataLoggingInterval invalidate];
        
    }
    
}


-(void)logValues:(id)sender
{

    /*
    NSString *errorDesc = nil;
    NSPropertyListFormat format;
    NSString *plistPath;
    NSString *rootPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,
                                                              NSUserDomainMask, YES) objectAtIndex:0];
    plistPath = [rootPath stringByAppendingPathComponent:@"Data.plist"];
    if (![[NSFileManager defaultManager] fileExistsAtPath:plistPath]) {
        plistPath = [[NSBundle mainBundle] pathForResource:@"Data" ofType:@"plist"];
    }
    NSData *plistXML = [[NSFileManager defaultManager] contentsAtPath:plistPath];
    NSDictionary *temp = (NSDictionary *)[NSPropertyListSerialization
                                          propertyListFromData:plistXML
                                          mutabilityOption:NSPropertyListMutableContainersAndLeaves
                                          format:&format
                                          errorDescription:&errorDesc];
    if (!temp) {
        NSLog(@"Error reading plist: %@, format: %d", errorDesc, format);
    }
    NSMutableArray *newArray = [temp objectForKey:@"x"];
    //NSLog([NSString stringWithFormat:@"%@", newArray]);
    
    
    //load from savedStock example int value
    */

    [self.xArray addObject:[NSString stringWithFormat:@"%f", self.accelerationX]];
    [self.yArray addObject:[NSString stringWithFormat:@"%f", self.accelerationY]];
    [self.yArray addObject:[NSString stringWithFormat:@"%f", self.accelerationZ]];
    
    
    //NSLog([NSString stringWithFormat:@"%@", newArray]);
    
}



-(void)flushAccelerometerData
{
    NSString *error;
    NSString *rootPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
    NSString *plistPath = [rootPath stringByAppendingPathComponent:@"Data.plist"];
    NSDictionary *plistDict = [NSDictionary dictionaryWithObjects:
                               [NSArray arrayWithObjects: self.xArray, self.yArray, self.zArray, nil]
                                                          forKeys:[NSArray arrayWithObjects: @"x", @"y", @"z", nil]];
    NSData *plistData = [NSPropertyListSerialization dataFromPropertyList:plistDict
                                                                   format:NSPropertyListXMLFormat_v1_0
                                                         errorDescription:&error];
    if(plistData) {
        [plistData writeToFile:plistPath atomically:YES];
    }
    else {
        NSLog(error);
    }
    
    
    
    
    
    
    

    

    
    
}
-(void)outputAccelerationData:(CMAcceleration)acceleration
{
    NSLog(@"I'm getting called at all");
    
    
    self.accX.text = [NSString stringWithFormat:@" %.2fg",acceleration.x];
    if(fabs(acceleration.x) > fabs(currentMaxAccelX))
    {
        currentMaxAccelX = acceleration.x;
    }
    self.accY.text = [NSString stringWithFormat:@" %.2fg",acceleration.y];
    if(fabs(acceleration.y) > fabs(currentMaxAccelY))
    {
        currentMaxAccelY = acceleration.y;
    }
    self.accZ.text = [NSString stringWithFormat:@" %.2fg",acceleration.z];
    if(fabs(acceleration.z) > fabs(currentMaxAccelZ))
    {
        currentMaxAccelZ = acceleration.z;
    }
    
    self.accelerationX = acceleration.x;
    self.accelerationX = acceleration.y;
    self.accelerationX = acceleration.z;
    
    NSLog([NSString stringWithFormat:@"x: %f \ny: %f \nz: %f", acceleration.x, acceleration.y, acceleration.z]);
    
    self.maxAccX.text = [NSString stringWithFormat:@" %.2f",currentMaxAccelX];
    self.maxAccY.text = [NSString stringWithFormat:@" %.2f",currentMaxAccelY];
    self.maxAccZ.text = [NSString stringWithFormat:@" %.2f",currentMaxAccelZ];
    
    
}
-(void)outputRotationData:(CMRotationRate)rotation
{
    
    self.rotX.text = [NSString stringWithFormat:@" %.2fr/s",rotation.x];
    if(fabs(rotation.x) > fabs(currentMaxRotX))
    {
        currentMaxRotX = rotation.x;
    }
    self.rotY.text = [NSString stringWithFormat:@" %.2fr/s",rotation.y];
    if(fabs(rotation.y) > fabs(currentMaxRotY))
    {
        currentMaxRotY = rotation.y;
    }
    self.rotZ.text = [NSString stringWithFormat:@" %.2fr/s",rotation.z];
    if(fabs(rotation.z) > fabs(currentMaxRotZ))
    {
        currentMaxRotZ = rotation.z;
    }
    
    self.maxRotX.text = [NSString stringWithFormat:@" %.2f",currentMaxRotX];
    self.maxRotY.text = [NSString stringWithFormat:@" %.2f",currentMaxRotY];
    self.maxRotZ.text = [NSString stringWithFormat:@" %.2f",currentMaxRotZ];
}

- (IBAction)resetMaxValues:(id)sender {
    
    currentMaxAccelX = 0;
    currentMaxAccelY = 0;
    currentMaxAccelZ = 0;
    
    currentMaxRotX = 0;
    currentMaxRotY = 0;
    currentMaxRotZ = 0;
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
