.DEFAULT_GOAL := help

.PHONY: deploy
deploy: test docs build ## Deploy to production
	@echo "Deploying to production..."
    # Add your deployment commands here

.PHONY: test
test: ## Run tests
	@echo "Running tests..."
    # Add your test commands here

.PHONY: docs
docs: ## Generate documentation
	@echo "Generating documentation...."
    # Add your documentation commands here

.PHONY: build
build: ## Build the project
	@echo "Building the project..."
    # Add your build commands here

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
