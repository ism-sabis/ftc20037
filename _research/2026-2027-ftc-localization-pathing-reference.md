# FTC localization and pathing terms

**Checked:** 2026-11-21  
**Purpose:** Help identify the robot team's transcribed terms “dormitory pods” and “Aspen.” These are possible matches, not confirmation of the team's chosen hardware or software.

**Team follow-up:** The user confirmed **Pedro Pathing** as the planned pathing software, **7075 aluminum** panels, **goBILDA odometry pods** with an **IMU**, and that the turret-mounted **Limelight is for aiming the turret**. The exact pod model/IMU arrangement and Limelight vision mode/target remain unconfirmed. “Aspen” remains unresolved. The user prefers general public wording: “odometry pod and IMU.”

## Likely term: odometry pods

“Dormitory pods” is very likely a speech-to-text error for **odometry pods**. In FTC, these are usually tracking-wheel assemblies with encoders that measure robot travel for localization. goBILDA describes its pods as measuring travel and its Pinpoint Odometry Computer as combining pod inputs to estimate the robot's heading and field position. [goBILDA Odometry](https://www.gobilda.com/odometry)

The broader term **odometry** means estimating position from measured movement. Road Runner's current FTC tuning guide supports drive encoders, two- or three-wheel “dead wheel” localizers, goBILDA Pinpoint, and SparkFun OTOS. Its guide calls out mecanum-drive tuning separately. [Road Runner Tuning](https://rr.brott.dev/docs/v1-0/tuning/)

## Candidate software names

| Name | What it does | Primary documentation |
| --- | --- | --- |
| **Road Runner** | FTC motion-planning and path-following library. Its FTC tuning guide includes multiple localization choices, including dead wheels and Pinpoint. | [Road Runner Docs](https://rr.brott.dev/docs/v1-0/tuning/) |
| **Pedro Pathing** | FTC autonomous path-following library. Its official docs describe following Bézier-curve paths and tuning a localizer. | [Pedro Pathing Docs](https://pedropathing.com/docs) |
| **Limelight / AprilTag localization** | Vision hardware and software that can track AprilTags and estimate robot pose. This can provide localization or vision input; it is distinct from a path-following library such as Road Runner or Pedro Pathing. | [Limelight 3 Quick-Start](https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3) |
| **Pinpoint / OTOS** | Localization hardware/sensor options referenced by Road Runner. Pinpoint fuses pod readings; OTOS is an optical tracking sensor. | [goBILDA Odometry](https://www.gobilda.com/odometry), [Road Runner Tuning](https://rr.brott.dev/docs/v1-0/tuning/) |

## “Aspen” remains unresolved

The exact name **Aspen** did not match a primary FTC localization or pathing project in this lookup. It could be a transcription error, a team-specific name, or a different product. The closest likely recall prompts from the robot context are **Road Runner**, **Pedro Pathing**, or **Limelight AprilTag localization**. Road Runner's official docs also name **OTOS**, but it is a tracking sensor rather than the pathing software.

## Useful follow-up questions

1. Did “dormitory pods” mean **odometry pods** or tracking wheels for robot localization?
2. Which target and vision mode does the Limelight use for turret aiming? Is “dormitory pods” the team's term for odometry/tracking-wheel pods?
3. If “Aspen” still sounds right, can the team check the code repository, Android Studio dependency list, or a teammate's notes for its spelling?
