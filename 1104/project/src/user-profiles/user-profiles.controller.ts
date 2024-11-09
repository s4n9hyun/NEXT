// src/user-profiles/user-profiles.controller.ts
import {
  Controller,
  Post,
  Get,
  Put,
  Body,
  UseGuards,
  Request,
} from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { UserProfilesService } from './user-profiles.service';

@Controller('profiles')
export class UserProfilesController {
  constructor(private readonly userProfilesService: UserProfilesService) {}

  @UseGuards(AuthGuard('jwt'))
  @Post()
  async createProfile(@Request() req, @Body() { bio, avatarUrl }) {
    return this.userProfilesService.createProfile(req.user.id, bio, avatarUrl);
  }

  @UseGuards(AuthGuard('jwt'))
  @Get()
  async getProfile(@Request() req) {
    return this.userProfilesService.getProfile(req.user.id);
  }

  @UseGuards(AuthGuard('jwt'))
  @Put()
  async updateProfile(@Request() req, @Body() { bio, avatarUrl }) {
    return this.userProfilesService.updateProfile(req.user.id, bio, avatarUrl);
  }
}
