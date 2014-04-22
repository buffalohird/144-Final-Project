//
//  ThirdViewController.m
//  SmarteRun
//
//  Created by Buffalo Hird on 4/21/14.
//  Copyright (c) 2014 Buffalo Hird. All rights reserved.
//

#import "ThirdViewController.h"

@interface ThirdViewController ()

@end

@implementation ThirdViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    // Do any additional setup after loading the view.
}

- (void)submitGoals
{
    NSString *distanceString = [[NSString alloc] init];
    distanceString = self.estimatedDistanceField.text;
    
    NSString *paceString = [[NSString alloc] init];
    paceString = self.estimatedPaceField.text;
    
    
    RunViewController *runViewController = [[RunViewController alloc] init];
    runViewController.distance = distanceString;
    runViewController.pace = paceString;
    runViewController.modalTransitionStyle = UIModalTransitionStyleCoverVertical;
    [self presentViewController:runViewController animated:YES completion:nil];


}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
