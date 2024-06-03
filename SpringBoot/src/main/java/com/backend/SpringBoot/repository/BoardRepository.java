package com.backend.SpringBoot.repository;

import com.backend.SpringBoot.domain.Article;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BoardRepository extends JpaRepository<Article, Long> {
}