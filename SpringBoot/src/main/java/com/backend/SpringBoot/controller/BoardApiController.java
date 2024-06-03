package com.backend.SpringBoot.controller;

import com.backend.SpringBoot.domain.Article;
import com.backend.SpringBoot.dto.AddArticleRequest;
import com.backend.SpringBoot.dto.ArticleResponse;
import com.backend.SpringBoot.dto.UpdateArticleRequest;
import com.backend.SpringBoot.service.BoardService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class BoardApiController {
    private final BoardService boardService;

    @PostMapping("/api/articles")
    public ResponseEntity<Article> addArticle(@RequestBody AddArticleRequest request) {
        Article savedArticle = boardService.save(request);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(savedArticle);
    }

    @GetMapping("/api/articles")
    public ResponseEntity<List<ArticleResponse>> findAllArticles() {
        List<ArticleResponse> articles = boardService.findAll()
                .stream()
                .map(ArticleResponse::new)
                .toList();

        return ResponseEntity.ok()
                .body(articles);
    }

    @GetMapping("/api/articles/{id}")

    public ResponseEntity<ArticleResponse> findArticle(@PathVariable long id) {
        Article article = boardService.findById(id);

        return ResponseEntity.ok()
                .body(new ArticleResponse(article));
    }

    @DeleteMapping("/api/articles/{id}")
    public ResponseEntity<Void> deleteArticle(@PathVariable long id) {
        boardService.delete(id);

        return ResponseEntity.ok()
                .build();
    }

    @PutMapping("/api/articles/{id}")
    public ResponseEntity<Article> updateArticle(@PathVariable long id,
                                                 @RequestBody UpdateArticleRequest request) {
        Article updatedArticle = boardService.update(id, request);

        return ResponseEntity.ok()
                .body(updatedArticle);
    }
}
