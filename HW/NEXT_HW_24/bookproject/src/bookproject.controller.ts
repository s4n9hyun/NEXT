import {
  Controller,
  Param,
  Body,
  Delete,
  Get,
  Post,
  Put,
} from '@nestjs/common';
import { BookProjectService } from './bookproject.service';

@Controller('bookproject')
export class BookProjectController {
  bookProjectService: BookProjectService;
  constructor() {
    this.bookProjectService = new BookProjectService();
  }

  @Get()
  getAllPosts() {
    console.log('모든 게시글 가져오기');
    return this.bookProjectService.getAllPosts();
  }

  @Post()
  createPost(@Body() postDto) {
    console.log('게시글 작성');
    this.bookProjectService.createPost(postDto);
    return 'success';
  }

  @Get('/:id')
  getPost(@Param('id') id: string) {
    console.log(['게시글 하나 가져오기']);
    return this.bookProjectService.getPost(id);
  }

  @Delete('/:id')
  deletePost(@Param('id') id: string) {
    console.log('게시글 삭제');
    this.bookProjectService.delete(id);
    return 'success';
  }

  @Put('/:id')
  updatePost(@Param('id') id: string, @Body() postDto) {
    console.log('게시글 업데이트', id, postDto);
    return this.bookProjectService.updatePost(id, postDto);
  }
}
