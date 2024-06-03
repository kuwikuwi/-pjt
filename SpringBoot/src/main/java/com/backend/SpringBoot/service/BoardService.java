package com.backend.SpringBoot.service;

import com.backend.SpringBoot.domain.Article;
import com.backend.SpringBoot.dto.AddArticleRequest;
import com.backend.SpringBoot.dto.UpdateArticleRequest;
import com.backend.SpringBoot.repository.BoardRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
public class BoardService {
    private final BoardRepository boardRepository;
    public Article save(AddArticleRequest request) {
        return boardRepository.save(request.toEntity());
    }

    public List<Article> findAll() {
        return boardRepository.findAll();
    }

    public Article findById(long id) {
        return boardRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("not found" + id));
    }

    public void delete(long id) {
        boardRepository.deleteById(id);
    }

    @Transactional
    public Article update(long id, UpdateArticleRequest request) {
        Article article = boardRepository.findById(id)
                .orElseThrow(()-> new IllegalArgumentException("not found" + id));

        article.update(request.getTitle(), request.getContent());

        return article;
    }
}
