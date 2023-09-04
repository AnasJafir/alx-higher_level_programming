#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the linked list
 * Return: 0 if no cycle, 1 if there's a cycle
*/
int check_cycle(listint_t *list)
{
	/*Defining two pointers to the first node*/
	listint_t *first_ptr = list; /*a pointer to browse the list by one node */
	listint_t *second_ptr = list; /*a ponter to browse the list by two nodes */

	if (!list)
		return (0);
	while (first_ptr && second_ptr && second_ptr->next)
	{
		first_ptr = first_ptr->next;
		second_ptr = second_ptr->next->next;
		if (first_ptr == second_ptr)
			return (1);
	}
	return (0);
}
