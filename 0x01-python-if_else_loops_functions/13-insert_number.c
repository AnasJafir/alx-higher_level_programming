#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number in a sorted linked list
 * @head: pointer to the head of the list
 * @number: the number to insert
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current, *prev;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = current;
	return (new_node);
}
