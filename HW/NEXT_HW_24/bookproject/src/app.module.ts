import { Module } from '@nestjs/common';
import { BookProjectController } from './bookproject.controller';
import { BookProjectService } from './bookproject.service';

@Module({
  imports: [],
  controllers: [BookProjectController],
  providers: [BookProjectService],
})
export class AppModule {}
